from playwright.sync_api import Page


class LandingPage:
    def __init__(self, page: Page):
        self.page = page
        self.lead_form = page.get_by_role("button", name="Aperte o play... se tiver coragem")
        self.modal_title = page.get_by_role("heading", name="Fila de espera")
        self.name_input = page.get_by_placeholder("Informe seu nome")
        self.email_input = page.get_by_placeholder("Informe seu email")
        self.submit_button = page.get_by_role("button", name="Quero entrar na fila!")
        self.email_error = page.locator(".alert").get_by_text("Email incorreto")
        self.blank_field_error = page.locator(".alert").get_by_text("Campo obrigatório")
        self.success_message = page.get_by_text("Agradecemos por compartilhar seus dados")
        self.duplicated_email_error = page.get_by_text("já está registrado")

    def visit(self):
        self.page.goto("http://localhost:3000")

    def open_lead_form_button(self):
        self.lead_form.click()

    def submit_lead_form(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.submit_button.click()
