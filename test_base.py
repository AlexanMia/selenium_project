from .util.locators import MainPage
from .pages.base_page import BasePage
from .util.constants import Constants


class TestBase:
    def init_page(self, browser):
        global page
        page = BasePage(browser, Constants.link_1)
        return page

    def open_page(self):
        global page
        page.open()

    def check_title(self):
        global page
        assert page.get_page_title() == Constants.PAGE_TITLE, f"Title is not {Constants.PAGE_TITLE}"

    def get_to_log_in(self):
        global page
        page.element_click(MainPage.LOGIN)
        page.enter_value_into_box(MainPage.LOG, Constants.user_name)
        page.enter_value_into_box(MainPage.PASSWORD, Constants.password)
        page.element_click(MainPage.BUTTON_ENTER)

    def check_proper_user(self):
        # POINT 4
        global page
        assert page.get_elements_text(MainPage.NAME_USER) == Constants.NAME_USER, \
            f"User's name is not {Constants.NAME_USER}"
