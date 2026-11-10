import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

pytestmark = pytest.mark.checkout


@pytest.mark.smoke
def test_complete_checkout(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item("sauce-labs-backpack")
    inventory.go_to_cart()

    CartPage(logged_in_page).checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_details("Supritha", "Test", "30301")
    checkout.finish()

    expect(checkout.complete_header).to_have_text("Thank you for your order! ")


@pytest.mark.parametrize("first, last, postal, error_message", [
    ("", "Test", "30301", "First Name is required"),
    ("Supritha", "", "30301", "Last Name is required"),
    ("Supritha", "Test", "", "Postal Code is required"),
], ids=["no_first_name", "no_last_name", "no_postal_code"])
def test_checkout_missing_details(logged_in_page, first, last, postal, error_message):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item("sauce-labs-backpack")
    inventory.go_to_cart()
    CartPage(logged_in_page).checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_details(first, last, postal)

    expect(checkout.error).to_contain_text(error_message)