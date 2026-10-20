from playwright.sync_api import Page, expect

class LoginPage():
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('.login-form').get_by_placeholder('E-mail')
        self.pwd_input = page.locator('.login-form').get_by_placeholder('Senha')
        self.submit_button = page.get_by_role('button', name='Entrar')
        self.email_error = page.get_by_text('Email incorreto')
        self.login_error = page.get_by_text('Ocorreu um erro ao tentar efetuar o login')
        self.blank_email_field_error = page.locator(".email-alert").get_by_text("Campo obrigatório")
        self.blank_pwd_field_error = page.locator(".password-alert").get_by_text("Campo obrigatório")

    def visit(self):
        self.page.goto("http://localhost:3000/admin/login")

    def submit(self, email, pwd):
        self.email_input.fill(email)
        self.pwd_input.fill(pwd)
        self.submit_button.click()