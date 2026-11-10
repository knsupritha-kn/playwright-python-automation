import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username", [
    "standard_user",
    "problem_user",
    "visual_user",
])
def test_valid_login(page: Page, username):
    login = LoginPage(page)
    login.open()
    login.login(username, "secret_sauce")
    expect(InventoryPage(page).title).to_have_text("Products")


@pytest.mark.login
@pytest.mark.parametrize("username, password, error_message", [
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
    ("standard_user", "wrong_pass", "Username and password do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
])
def test_invalid_login(page: Page, username, password, error_message):
    login = LoginPage(page)
    login.open()
    login.login(username, password)
    expect(login.error).to_contain_text(error_message)