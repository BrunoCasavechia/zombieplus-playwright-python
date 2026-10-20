from faker import Faker
from playwright.sync_api import expect

from pages.landing_page import LandingPage

fake = Faker("pt_BR")


def test_success(page):
    name_fake = fake.name()
    email_fake = fake.email()

    lead = LandingPage(page)
    lead.visit()
    lead.open_lead_form_button()
    lead.submit_lead_form(name_fake, email_fake)

    expect(lead.success_message).to_be_visible()


def test_name_blank(page):
    email_fake = fake.email()

    lead = LandingPage(page)
    lead.visit()
    lead.open_lead_form_button()
    lead.submit_lead_form("", email_fake)

    expect(lead.blank_field_error).to_be_visible()


def test_email_blank(page):
    name_fake = fake.name()

    lead = LandingPage(page)
    lead.visit()
    lead.open_lead_form_button()
    lead.submit_lead_form(name_fake, "")

    expect(lead.blank_field_error).to_be_visible()


def test_email_error(page):
    name_fake = fake.name()

    lead = LandingPage(page)
    lead.visit()
    lead.open_lead_form_button()
    lead.submit_lead_form(name_fake, "zombieplus.com")

    expect(lead.email_error).to_be_visible()


def test_email_duplicated(page):
    name_fake = fake.name()
    email_fake = fake.email()

    lead = LandingPage(page)

    # first sign up works
    lead.visit()
    lead.open_lead_form_button()
    lead.submit_lead_form(name_fake, email_fake)

    # same email again should be blocked
    lead.visit()
    lead.open_lead_form_button()
    lead.submit_lead_form(name_fake, email_fake)

    expect(lead.duplicated_email_error).to_be_visible()
