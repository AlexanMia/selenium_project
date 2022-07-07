import pytest
from .test_base import TestBase
from util.locators import MainPage, DifferentElements
from util.constants import Constants


class Test2(TestBase):
    def test_open_site_with_proper_title(self, browser):
        # POINT 1, 2
        global page
        page = super().init_page(browser)
        super().open_page()
        super().check_title()

    def test_log_in_with_proper_user(self, browser):
        # POINT 3, 4
        super().get_to_log_in()
        super().check_proper_user()

    def test_is_elements_service_exist(self):
        # POINT 5
        global page
        page.element_click(MainPage.service)
        service_items = [page.find_need_element(MainPage.SUPPORT_UNDER_SERVICE),
                         page.find_need_element(MainPage.DATES_UNDER_SERVICE),
                         page.find_need_element(MainPage.COMPLEX_TABLE_UNDER_SERVICE),
                         page.find_need_element(MainPage.SIMPLE_TABLE_UNDER_SERVICE),
                         page.find_need_element(MainPage.TABLE_WITH_PAGES_UNDER_SERVICE),
                         page.find_need_element(MainPage.DIFFERENT_ELEMENTS_UNDER_SERVICE)
                         ]
        for i in service_items:
            assert i, 'Option is not existed'

    def test_is_elements_left_section_exist(self):
        # POINT 6
        global page
        page.element_click(MainPage.SERVICE_ON_THE_LEFT)
        service_items_on_the_left = [page.find_need_element(MainPage.SUPPORT_SERVICE_ON_THE_LEFT),
                                     page.find_need_element(MainPage.DATES_SERVICE_ON_THE_LEFT),
                                     page.find_need_element(MainPage.COMPLEX_TABLE_SERVICE_ON_THE_LEFT),
                                     page.find_need_element(MainPage.SIMPLE_TABLE_SERVICE_ON_THE_LEFT),
                                     page.find_need_element(MainPage.TABLE_WITH_PAGES_SERVICE_ON_THE_LEFT),
                                     page.find_need_element(MainPage.DIFFERENT_ELEMENTS_SERVICE_ON_THE_LEFT)
                                     ]

        for i in service_items_on_the_left:
            assert i, 'Option is not existed'

    def test_open_different_elements_page(self):
        # POINT 7
        global page
        page.element_click(MainPage.service)
        page.element_click(MainPage.DIFFERENT_ELEMENTS_UNDER_SERVICE)

    def test_are_all_elements_exist(self):
        # POINT 8
        global page
        needed_elements = {Constants.EXPECTED_NUMBERS_OF_CHECKBOXES: page.find_elements_all(DifferentElements.CHECKBOXES),
                           Constants.EXPECTED_NUMBERS_OF_RADIOS: page.find_elements_all(DifferentElements.RADIOS),
                           Constants.EXPECTED_NUMBERS_OF_DROP_DOWN: page.find_elements_all(DifferentElements.DROP_DOWN),
                           Constants.EXPECTED_NUMBERS_OF_BUTTONS: [page.find_elements_all(DifferentElements.BUTTON_DEFAULT),
                                                                   page.find_elements_all(DifferentElements.BUTTON_UII)]}

        for i, j in needed_elements.items():
            assert i == int(len(j)), 'Not all elements exist'

    def test_right_section_of_dif_elems_is_displayed(self):
        # POINT 9
        global page
        assert page.find_need_element(DifferentElements.RIGHT_SECTION), 'Right section is not displayed'

    def test_left_section_of_dif_elems_is_displayed(self):
        # POINT 10
        global page
        assert page.find_need_element(DifferentElements.LEFT_SECTION), 'Left section is not displayed'

    @pytest.mark.parametrize('loc_checkbox,loc_logs,global_meaning', [
        (DifferentElements.CHECKBOX_WATER, DifferentElements.LOGS, Constants.WATER),
        (DifferentElements.CHECKBOX_WIND, DifferentElements.LOGS, Constants.WIND)
    ])
    def test_selecting_checkboxes_have_logs_and_select(self, loc_checkbox, loc_logs, global_meaning):
        # POINT 11, 12
        global page
        page.element_click(loc_checkbox)
        assert page.find_need_element(loc_logs), 'Log is not presented'
        assert page.is_text_found(loc_logs, global_meaning) and \
               page.is_text_found(loc_logs, 'true'), 'Text is not expected'


    def test_selecting_radios_have_logs_and_select(self):
        # POINT 13, 14
        global page
        page.element_click(DifferentElements.RADIO_SELEN)
        assert page.is_element_selected(DifferentElements.RADIO_SELEN), 'Radio does not be chosen'
        assert page.find_need_element(DifferentElements.LOGS), 'Log is not presented'
        assert page.is_text_found(DifferentElements.LOGS, Constants.SELEN), 'Text is not expected'

    def test_selecting_dropdown_have_logs_and_select(self):
        # POINT 15, 16
        global page
        page.element_click(DifferentElements.DROP_DOWN_YELLOW)
        assert page.is_element_selected(DifferentElements.DROP_DOWN_YELLOW), f'Drop down {Constants.YELLOW} does not be chosen'
        assert page.find_need_element(DifferentElements.LOGS), "Log is not presented"
        assert page.is_text_found(DifferentElements.LOGS, Constants.YELLOW), 'Text is not expected'

    @pytest.mark.parametrize('loc_checkbox,loc_logs,loc_global_meaning', [
        (DifferentElements.CHECKBOX_WATER, DifferentElements.LOGS, Constants.WATER),
        (DifferentElements.CHECKBOX_WIND, DifferentElements.LOGS, Constants.WIND)
    ])
    def test_unselect_checkboxes_have_logs_and_unselect(self, loc_checkbox, loc_logs, loc_global_meaning):
        # POINT 17, 18
        global page
        page.element_click(loc_checkbox)
        assert not page.is_element_selected(loc_checkbox), 'Checkbox is chosen'
        assert page.find_need_element(loc_logs), "Log is not presented"
        assert page.is_text_found(loc_logs, loc_global_meaning) and \
               page.is_text_found(loc_logs, 'false'), 'Text is not expected'