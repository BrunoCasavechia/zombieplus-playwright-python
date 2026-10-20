from pages.login_page import LoginPage


def test_login_admin(page):
    login = LoginPage(page)
    login.visit()
