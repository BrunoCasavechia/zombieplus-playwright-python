from pages.login_page import LoginPage
from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker('pt_br')

email = 'admin@zombieplus.com'
pwd = 'pwd123'

def test_login_success(page):
    login = LoginPage(page)

    login.visit()
    login.submit(email, pwd)

def test_unregistered_user(page):
    email_fake = fake.email()
    pwd_fake = fake.password()
     
    login = LoginPage(page)
    
    login.visit()
    login.submit(email_fake, pwd_fake)

    expect(login.login_error).to_be_visible()


def test_blank_email(page):
    login = LoginPage(page)

    login.visit()
    login.submit('', pwd)

    expect(login.blank_email_field_error).to_be_visible()


def test_blank_pwd(page):
    login = LoginPage(page)

    login.visit()
    login.submit(email, '')

    expect(login.blank_pwd_field_error).to_be_visible()


def test_email_error(page):
    login = LoginPage(page)

    login.visit()
    login.submit('emailinvalid.com', pwd)

    expect(login.email_error).to_be_visible()


def test_pwd_invalid(page):
    login = LoginPage(page)

    login.visit()
    login.submit(email, 'invalidpwd')

    expect(login.login_error).to_be_visible()



