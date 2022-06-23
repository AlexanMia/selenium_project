import pytest
from .pages.locators import BasePageLocators
from .pages.global_meaning import GlobalMeaning
from .pages.base_page import BasePage


class Test1:
    def test_open_test_site(self, browser):
        global page
        link = "https://jdi-testing.github.io/jdi-light/index.html"
        page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу


    def test_proper_title(self):
        # POINT 2
        global page
        assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"

    def test_logging(self, browser):
        # CHECKED
        # POINT 3
        # LOG IN
        global page
        page.element_click(BasePageLocators.LOGIN)
        page.enter_value_into_box(BasePageLocators.LOG, GlobalMeaning.user_name)
        page.enter_value_into_box(BasePageLocators.PASSWORD, GlobalMeaning.password)
        page.element_click(BasePageLocators.BUTTON_ENTER)

    def test_proper_name_user(self, browser):
        # POINT 4
        global page
        assert page.find_element_1(BasePageLocators.NAME_USER).text == GlobalMeaning.NAME_USER, \
            f"User's name is not {GlobalMeaning.NAME_USER}"

    def test_proper_title(self, browser):
        # CHECKED
        # POINT 5
        global page
        assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"


    def test_is_items_and_propers_text(self, browser):
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

    def test_is_four_images(self, browser):
        # CHECKED
        # POINT 7
        global page
        images_locators = [BasePageLocators.IMAGE_1,
                           BasePageLocators.IMAGE_2,
                           BasePageLocators.IMAGE_3,
                           BasePageLocators.IMAGE_4]
        assert all([page.search_element_m(i) for i in images_locators]), 'Not all elements are showed'

    def test_are_four_texts_under_images(self, browser):
        # CHECKED
        # POINT 8
        global page
        texts_locators = [BasePageLocators.TEXT_1, BasePageLocators.TEXT_2, BasePageLocators.TEXT_3,
                          BasePageLocators.TEXT_4]
        expected_texts = [GlobalMeaning.TEXT_UNDER_PICT_1, GlobalMeaning.TEXT_UNDER_PICT_2,
                          GlobalMeaning.TEXT_UNDER_PICT_3,
                          GlobalMeaning.TEXT_UNDER_PICT_4]
        actual_texts = []
        [actual_texts.append(page.get_elements_text(i).replace('\n', ' ')) for i in texts_locators]
        assert all([a == b for a, b in zip(actual_texts, expected_texts)]), 'Texts are not equal'

    def test_is_text_of_the_main_headers(self, browser):
        # CHECKED
        # POINT 9
        global page
        texts_of_main_page = {
            page.search_element_m(BasePageLocators.TEXT_of_the_MAIN_PAGE_1).text: GlobalMeaning.TEXT_ON_MAIN_PAGE_1,
            page.search_element_m(BasePageLocators.TEXT_of_the_MAIN_PAGE_2).text: GlobalMeaning.TEXT_ON_MAIN_PAGE_2
            }
        for i, j in texts_of_main_page.items():
            assert i == j, f'Texts is not equal {i} = {j}'

    def test_is_the_iframe(self, browser):
        # CHECKED
        # POINT 10
        global page
        assert page.search_element_m(BasePageLocators.IFRAME), 'Iframe is not be found'

    def test_switch_to_iframe(self, browser):
        # CHECKED
        # POINT 11
        global page
        browser.switch_to.frame('frame')
        assert page.search_element_m(BasePageLocators.IFRAME_BUTTON), 'Iframe button is not be found'

    def test_switch_to_original_window(self, browser):
        # CHECKED
        # POINT 12
        global page
        browser.switch_to.default_content()
        assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).text == GlobalMeaning.TEXT_OF_SUB_HEADER, \
            'Exit from frame is unsuccessful'

    def test_proper_text_of_the_header(self, browser):
        # CHECKED
        # POINT 13
        global page
        assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).text == GlobalMeaning.TEXT_OF_SUB_HEADER, \
            'Texts are not equal'

    def test_proper_link(self, browser):
        # CHECKED
        # POINT 14
        global page
        assert page.search_element_m(BasePageLocators.TEXT_OF_SUB).get_attribute('href') == GlobalMeaning.LINK, \
            'Links are not equal'

    def test_is_left_section(self, browser):
        # CHECKED
        # POINT 15
        global page
        assert page.search_element_m(BasePageLocators.LEFT_SECTION), 'Left section is not displayed'

    def test_is_footer(self, browser):
        # CHECKED
        # POINT 16
        global page
        assert page.search_element_m(BasePageLocators.FOOTER), 'Footer is not displayed'



