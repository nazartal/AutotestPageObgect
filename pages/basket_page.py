from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_add_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Basket is not empty"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"