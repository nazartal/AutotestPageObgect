from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    
    def push_add_in_basket(self):
        add_in_basket = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        add_in_basket.click()
        
    def check_what_add_right_book_with_right_price(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        prise_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        message_add_name_book = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_NAME_BOOK).text
        message_add_prise_book = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_PRICE_BOOK).text
        assert name_book == message_add_name_book, "добавлена не та книга"
        assert prise_book == message_add_prise_book, "стоимость не совпадает"
        
        