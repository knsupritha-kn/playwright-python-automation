class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def add_item(self, item_name):
        self.page.locator(f'[data-test="add-to-cart-{item_name}"]').click()

    def remove_item(self, item_name):
        self.page.locator(f'[data-test="remove-{item_name}"]').click()

    def go_to_cart(self):
        self.cart_link.click()