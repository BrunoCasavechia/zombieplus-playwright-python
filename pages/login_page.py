from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_placeholder("E-mail")
        self.password_input = page.get_by_placeholder("Senha")
        self.submit_button = page.get_by_role("button", name="Entrar")

    def visit(self):
        self.page.goto("/admin/login")

    def submit(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
