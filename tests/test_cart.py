import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

pytestmark = pytest.mark.cart


def test_add_one_item(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item("sauce-labs-backpack")
    expect(inventory.cart_badge).to_have_text("1")


@pytest.mark.parametrize("items", [
    ["sauce-labs-backpack"],
    ["sauce-labs-backpack", "sauce-labs-bike-light"],
    ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"],
])
def test_add_multiple_items(logged_in_page, items):
    inventory = InventoryPage(logged_in_page)
    for item in items:
        inventory.add_item(item)
    inventory.go_to_cart()
    expect(CartPage(logged_in_page).items).to_have_count(len(items))


def test_remove_item(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item("sauce-labs-backpack")
    inventory.remove_item("sauce-labs-backpack")
    expect(inventory.cart_badge).to_be_hidden()