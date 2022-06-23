import pytest
from .pages.locators import BasePageLocators, DifferentElements
from .pages.global_meaning import GlobalMeaning
from .pages.base_page import BasePage
import time


class Test2:
    #@pytest.fixture(autouse=True)
    def test_open_test_site(self, browser):
        # POINT 1
        global page
        link = "https://jdi-testing.github.io/jdi-light/index.html"
        page = BasePage(browser, link)  # инициализируем Page Object,
        # передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

    def test_proper_title(self, browser):
        # POINT 2
        global page
        assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"

    def test_logging(self, browser):
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

    def test_is_elements_service_exist(self):
        # POINT 5
        global page
        page.element_click(BasePageLocators.service)
        service_items = [page.search_element_m(BasePageLocators.SUPPORT_UNDER_SERVICE),
                         page.search_element_m(BasePageLocators.DATES_UNDER_SERVICE),
                         page.search_element_m(BasePageLocators.COMPLEX_TABLE_UNDER_SERVICE),
                         page.search_element_m(BasePageLocators.SIMPLE_TABLE_UNDER_SERVICE),
                         page.search_element_m(BasePageLocators.TABLE_WITH_PAGES_UNDER_SERVICE),
                         page.search_element_m(BasePageLocators.DIFFERENT_ELEMENTS_UNDER_SERVICE)
                         ]
        for i in service_items:
            assert i, 'Option is not existed'

    def test_is_elements_left_section_exist(self):
        # POINT 6
        global page
        page.element_click(BasePageLocators.SERVICE_ON_THE_LEFT)
        service_items_on_the_left = [page.search_element_m(BasePageLocators.SUPPORT_SERVICE_ON_THE_LEFT),
                                     page.search_element_m(BasePageLocators.DATES_SERVICE_ON_THE_LEFT),
                                     page.search_element_m(BasePageLocators.COMPLEX_TABLE_SERVICE_ON_THE_LEFT),
                                     page.search_element_m(BasePageLocators.SIMPLE_TABLE_SERVICE_ON_THE_LEFT),
                                     page.search_element_m(BasePageLocators.TABLE_WITH_PAGES_SERVICE_ON_THE_LEFT),
                                     page.search_element_m(BasePageLocators.DIFFERENT_ELEMENTS_SERVICE_ON_THE_LEFT)
                                     ]

        for i in service_items_on_the_left:
            assert i, 'Option is not existed'

    def test_open_different_elements_page(self):
        # POINT 7
        global page
        page.element_click(BasePageLocators.service)
        page.element_click(BasePageLocators.DIFFERENT_ELEMENTS_UNDER_SERVICE)

    def test_are_all_elements_exist(self):
        # POINT 8
        global page
        needed_elements = {GlobalMeaning.NUMBERS_OF_CHECKBOXES: page.find_elements_all(DifferentElements.CHECKBOXES),
                           GlobalMeaning.NUMBERS_OF_RADIOS: page.find_elements_all(DifferentElements.RADIOS),
                           GlobalMeaning.NUMBERS_OF_DROP_DOWN: page.find_elements_all(DifferentElements.DROP_DOWN),
                           GlobalMeaning.NUMBERS_OF_BUTTONS: [page.find_elements_all(DifferentElements.BUTTON_1),
                                                              page.find_elements_all(DifferentElements.BUTTON_2)]}

        for i, j in needed_elements.items():
            # print(len(j))
            assert i == int(len(j)), 'Number of elements do not equal'

    def test_right_section_of_dif_elems_is_displayed(self):
        # POINT 9
        global page
        assert page.search_element_m(DifferentElements.RIGHT_SECTION), 'Right section is not displayed'

    def test_left_section_of_dif_elems_is_displayed(self):
        # POINT 10
        global page
        assert page.search_element_m(DifferentElements.LEFT_SECTION), 'Left section is not displayed'

    @pytest.mark.parametrize('loc_checkbox,loc_logs,global_meaning', [
        (DifferentElements.CHECKBOX_WATER, DifferentElements.LOGS, GlobalMeaning.WATER),
        (DifferentElements.CHECKBOX_WIND, DifferentElements.LOGS, GlobalMeaning.WIND)
    ])
    def test_selecting_checkboxes_have_logs_and_select(self, loc_checkbox, loc_logs, global_meaning):
        # POINT 11 b 12
        global page
        page.element_click(loc_checkbox)
        assert page.search_element_m(loc_logs), 'Log is not presented'
        assert page.is_text_found(loc_logs, global_meaning) and \
               page.is_text_found(loc_logs, 'true'), 'Text is not expected'


    def test_selecting_radios_have_logs_and_select(self):
        # POINT 13 и 14
        global page
        page.element_click(DifferentElements.RADIO_SELEN)
        assert page.is_element_selected(DifferentElements.RADIO_SELEN), 'Radio does not be chosen'
        assert page.search_element_m(DifferentElements.LOGS), 'Log is not presented'
        assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.SELEN), 'Text is not expected'

    def test_selecting_dropdown_have_logs_and_select(self):
        # POINT 15 и 16
        global page
        page.element_click(DifferentElements.DROP_DOWN_YELLOW)
        assert page.is_element_selected(DifferentElements.DROP_DOWN_YELLOW), 'Drop down yellow does not be chosen'
        assert page.search_element_m(DifferentElements.LOGS), "Log is not presented"
        assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.YELLOW), 'Text is not expected'

    @pytest.mark.parametrize('loc_checkbox,loc_logs,loc_global_meaning', [
        (DifferentElements.CHECKBOX_WATER, DifferentElements.LOGS, GlobalMeaning.WATER),
        (DifferentElements.CHECKBOX_WIND, DifferentElements.LOGS, GlobalMeaning.WIND)
    ])
    def test_unselect_checkboxes_have_logs_and_unselect(self, loc_checkbox, loc_logs, loc_global_meaning):
        # POINT 17 и 18
        global page
        page.element_click(loc_checkbox)
        time.sleep(5)
        assert not page.is_element_selected(loc_checkbox), 'Checkbox is chosen'
        assert page.search_element_m(loc_logs), "Log is not presented"
        assert page.is_text_found(loc_logs, loc_global_meaning) and \
               page.is_text_found(loc_logs, 'false'), 'Text is not expected'