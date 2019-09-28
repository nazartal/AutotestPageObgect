from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_IN_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ADD_NAME_BOOK = (By.CSS_SELECTOR, ".alert-success strong")
    MESSAGE_ADD_PRICE_BOOK = (By.CSS_SELECTOR, ".alert-info strong")