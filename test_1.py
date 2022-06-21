import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .pages.locators import BasePageLocators, MetalsColors
from .pages.global_meaning import GlobalMeaning
from .pages.base_page import BasePage
import time

from selenium.webdriver.support.select import Select


@pytest.mark.test1
def test_1(browser):
    link = "https://jdi-testing.github.io/jdi-light/index.html"
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    # POINT 2
    assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"


    # CHECKED
    # POINT 3
    # LOG IN
    page.element_click(BasePageLocators.LOGIN)
    page.enter_value_into_box(BasePageLocators.LOG, GlobalMeaning.user_name)
    page.enter_value_into_box(BasePageLocators.PASSWORD, GlobalMeaning.password)
    page.element_click(BasePageLocators.BUTTON_ENTER)
    # POINT 4
    assert page.find_element_1(BasePageLocators.NAME_USER).text == GlobalMeaning.NAME_USER, \
        f"User's name is not {GlobalMeaning.NAME_USER}"

    # CHECKED
    # POINT 5
    assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"

    # CHECKED
    # POINT 6
    items_locators = [BasePageLocators.home,
                      BasePageLocators.contact_form,
                      BasePageLocators.service,
                      BasePageLocators.metalscolours
                      ]
    expected_items_of_main_page = [GlobalMeaning.PROPER_TEXT_1,
                                   GlobalMeaning.PROPER_TEXT_2,
                                   GlobalMeaning.PROPER_TEXT_3,
                                   GlobalMeaning.PROPER_TEXT_4
                                   ]
    actual_texts_items = []
    [actual_texts_items.append(page.get_elements_text(i)) for i in items_locators]
    assert all([a == b for a, b in zip(actual_texts_items, expected_items_of_main_page)]), 'Texts are not equal'

    # CHECKED
    # POINT 7
    images_locators = [BasePageLocators.IMAGE_1,
                       BasePageLocators.IMAGE_2,
                       BasePageLocators.IMAGE_3,
                       BasePageLocators.IMAGE_4]
    assert all([page.search_element_m(i) for i in images_locators]), 'Not all elements are showed'

    # CHECKED
    # POINT 8
    texts_locators = [BasePageLocators.TEXT_1, BasePageLocators.TEXT_2, BasePageLocators.TEXT_3,
                      BasePageLocators.TEXT_4]
    expected_texts = [GlobalMeaning.TEXT_UNDER_PICT_1, GlobalMeaning.TEXT_UNDER_PICT_2, GlobalMeaning.TEXT_UNDER_PICT_3,
                      GlobalMeaning.TEXT_UNDER_PICT_4]
    actual_texts = []
    [actual_texts.append(page.get_elements_text(i).replace('\n', ' ')) for i in texts_locators]
    assert all([a == b for a, b in zip(actual_texts, expected_texts)]), 'Texts are not equal'

    # CHECKED
    # POINT 9
    texts_of_main_page = {page.search_element_m(BasePageLocators.TEXT_of_the_MAIN_PAGE_1).text: GlobalMeaning.TEXT_ON_MAIN_PAGE_1,
                          page.search_element_m(BasePageLocators.TEXT_of_the_MAIN_PAGE_2).text: GlobalMeaning.TEXT_ON_MAIN_PAGE_2
                          }
    for i, j in texts_of_main_page.items():
        assert i == j, f'Texts is not equal {i} = {j}'

    #CHECKED
    # POINT 10
    assert page.search_element_m(BasePageLocators.IFRAME), 'Iframe is not be found'

    # CHECKED
    # POINT 11
    browser.switch_to.frame('frame')
    assert page.search_element_m(BasePageLocators.IFRAME_BUTTON), 'Iframe button is not be found'

    # CHECKED
    # POINT 12
    browser.switch_to.default_content()
    assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).text == GlobalMeaning.TEXT_OF_SUB_HEADER, \
        'Exit from frame is unsuccessful'

    # CHECKED
    # POINT 13
    assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).text == GlobalMeaning.TEXT_OF_SUB_HEADER, \
        'Texts are not equal'

    # CHECKED
    # POINT 14
    assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).get_attribute('href') == GlobalMeaning.LINK, \
        'Links are not equal'

    # CHECKED
    # POINT 15
    assert page.search_element_m(BasePageLocators.LEFT_SECTION), 'Left section is not displayed'

    # CHECKED
    # POINT 16
    assert page.search_element_m(BasePageLocators.FOOTER), 'Footer is not displayed'


@pytest.mark.test1_a
class Test1:

    def test_open_test_site(self, browser):
        link = "https://jdi-testing.github.io/jdi-light/index.html"
        page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

    def test_proper_title(self, browser):

        # POINT 2

        assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"


    def test_logging(self, browser):
        # CHECKED
        # POINT 3
        # LOG IN
        page.element_click(BasePageLocators.LOGIN)
        page.enter_value_into_box(BasePageLocators.LOG, GlobalMeaning.user_name)
        page.enter_value_into_box(BasePageLocators.PASSWORD, GlobalMeaning.password)
        page.element_click(BasePageLocators.BUTTON_ENTER)

    def test_proper_name_user(self, page):
        # POINT 4
        assert page.find_element_1(BasePageLocators.NAME_USER).text == GlobalMeaning.NAME_USER, \
            f"User's name is not {GlobalMeaning.NAME_USER}"

    #def test_proper_title(self, browser):

        # CHECKED
        # POINT 5
        #assert self.browser.should_be_definite_title() == "Home Page", "Title is not Home Page"


    def test_is_items_and_propers_text(self, page):
        # CHECKED
        # POINT 6
        items_locators = [BasePageLocators.home,
                          BasePageLocators.contact_form,
                          BasePageLocators.service,
                          BasePageLocators.metalscolours
                          ]
        expected_items_of_main_page = [GlobalMeaning.PROPER_TEXT_1,
                                       GlobalMeaning.PROPER_TEXT_2,
                                       GlobalMeaning.PROPER_TEXT_3,
                                       GlobalMeaning.PROPER_TEXT_4
                                       ]
        actual_texts_items = []
        [actual_texts_items.append(page.get_elements_text(i)) for i in items_locators]
        assert all([a == b for a, b in zip(actual_texts_items, expected_items_of_main_page)]), 'Texts are not equal'


    def test_is_four_images(self, page):
        # CHECKED
        # POINT 7
        images_locators = [BasePageLocators.IMAGE_1,
                           BasePageLocators.IMAGE_2,
                           BasePageLocators.IMAGE_3,
                           BasePageLocators.IMAGE_4]
        assert all([page.search_element_m(i) for i in images_locators]), 'Not all elements are showed'


    def test_are_four_texts_under_images(self, page):
        # CHECKED
        # POINT 8
        texts_locators = [BasePageLocators.TEXT_1, BasePageLocators.TEXT_2, BasePageLocators.TEXT_3,
                          BasePageLocators.TEXT_4]
        expected_texts = [GlobalMeaning.TEXT_UNDER_PICT_1, GlobalMeaning.TEXT_UNDER_PICT_2,
                          GlobalMeaning.TEXT_UNDER_PICT_3,
                          GlobalMeaning.TEXT_UNDER_PICT_4]
        actual_texts = []
        [actual_texts.append(page.get_elements_text(i).replace('\n', ' ')) for i in texts_locators]
        assert all([a == b for a, b in zip(actual_texts, expected_texts)]), 'Texts are not equal'


    def test_is_text_of_the_main_headers(self, page):
        # CHECKED
        # POINT 9
        texts_of_main_page = {
            page.search_element_m(BasePageLocators.TEXT_of_the_MAIN_PAGE_1).text: GlobalMeaning.TEXT_ON_MAIN_PAGE_1,
            page.search_element_m(BasePageLocators.TEXT_of_the_MAIN_PAGE_2).text: GlobalMeaning.TEXT_ON_MAIN_PAGE_2
            }
        for i, j in texts_of_main_page.items():
            assert i == j, f'Texts is not equal {i} = {j}'

    def test_is_the_iframe(self, page):
        # CHECKED
        # POINT 10
        assert page.search_element_m(BasePageLocators.IFRAME), 'Iframe is not be found'


    def test_switch_to_iframe(self, page, browser):
        # CHECKED
        # POINT 11
        browser.switch_to.frame('frame')
        assert page.search_element_m(BasePageLocators.IFRAME_BUTTON), 'Iframe button is not be found'


    def test_switch_to_original_window(self, page, browser):
        # CHECKED
        # POINT 12
        browser.switch_to.default_content()
        assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).text == GlobalMeaning.TEXT_OF_SUB_HEADER, \
            'Exit from frame is unsuccessful'


    def test_proper_text_of_the_header(self, page):
        # CHECKED
        # POINT 13
        assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).text == GlobalMeaning.TEXT_OF_SUB_HEADER, \
            'Texts are not equal'


    def test_proper_link(self, page):
        # CHECKED
        # POINT 14
        assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).get_attribute('href') == GlobalMeaning.LINK, \
            'Links are not equal'


    def test_is_left_section(self, page):
        # CHECKED
        # POINT 15
        assert page.search_element_m(BasePageLocators.LEFT_SECTION), 'Left section is not displayed'


    def test_is_footer(self, page):
        # CHECKED
        # POINT 16
        assert page.search_element_m(BasePageLocators.FOOTER), 'Footer is not displayed'





