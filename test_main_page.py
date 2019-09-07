from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) 
    page.open()
    page.go_to_login_page()
    page2 = LoginPage(browser, link)
    page2.should_be_login_url()
    page2.should_be_login_form()
    page2.should_be_register_form()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()