import pytest
from selenium.webdriver.common.by import By
from util.locators import Locators, MetalsColors
from util.constants import Constants
from .pages.base_page import BasePage


class Test3:
    def test_open_test_site(self, browser):
        # POINT 1
        global page
        page = BasePage(browser, Constants.link_1)  # инициализируем Page Object,
        # передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

    def test_proper_title(self):
        # POINT 2
        global page
        assert page.get_page_title() == Constants.PAGE_TITLE, f"Title is not {Constants.PAGE_TITLE}"

    def test_logging(self, browser):
        # POINT 3
        # LOG IN
        global page
        page.element_click(Locators.LOGIN)
        page.enter_value_into_box(Locators.LOG, Constants.user_name)
        page.enter_value_into_box(Locators.PASSWORD, Constants.password)
        page.element_click(Locators.BUTTON_ENTER)

    def test_proper_name_user(self, browser):
        # POINT 4
        global page
        assert page.get_elements_text(Locators.NAME_USER) == Constants.NAME_USER, \
                f"User's name is not {Constants.NAME_USER}"

    def test_going_to_metals_colors(self):
        # POINT 5
        global page
        page.element_click(MetalsColors.metalscolours)

    @pytest.mark.parametrize('loc_radiobutton,loc_logs,global_meaning', [
        (MetalsColors.RADIO_5, MetalsColors.LOGS, Constants.NUMBER_5),
        (MetalsColors.RADIO_8, MetalsColors.LOGS, Constants.NUMBER_8)
    ])
    def test_radiobutton_have_logs_and_values(self, loc_radiobutton, loc_logs, global_meaning):
        # POINT 6, 7
        global page
        page.element_click(loc_radiobutton)
        assert page.find_need_element(loc_logs), "Log is not presented"
        assert page.get_elements_text(loc_logs).find(global_meaning), f"Number {global_meaning} is not found in the log"
        odd_even = "Even" if int(global_meaning) % 2 == 0 else "Odd"
        assert page.get_elements_text(loc_logs).find(odd_even), f"Number is not {odd_even}"

    def test_summary_result_in_logs(self):
        # POINT 8
        global page
        page.element_click(MetalsColors.CALCULATE_BUTTON)
        assert page.find_need_element(MetalsColors.LOGS), "Log is not presented"
        assert page.is_text_found(MetalsColors.CALCULATE_BUTTON_RESULTS, Constants.SUMMA) != -1, "Summa is not equal"

    @pytest.mark.parametrize('loc_checkbox,loc_selected_checkbox,loc_logs,global_meaning', [
        (MetalsColors.CHECKBOX_WATER, MetalsColors.SELECTED_CHECKBOX_WATER, MetalsColors.LOGS, Constants.WATER),
        (MetalsColors.CHECKBOX_WIND, MetalsColors.SELECTED_CHECKBOX_WIND, MetalsColors.LOGS, Constants.WIND)
    ])
    def test_select_checkboxes_have_logs_and_values(self, loc_checkbox, loc_selected_checkbox, loc_logs, global_meaning):
        # POINT 9-10
        global page
        page.element_click(loc_checkbox)
        assert page.is_element_selected(loc_selected_checkbox), 'Checkbox do not be chosen'
        assert page.find_need_element(loc_logs), "Log is not presented"
        assert page.is_text_found(loc_logs, global_meaning) and \
               page.is_text_found(loc_logs, 'true'), "Text is not expected"

    def test_select_dropdown_colors_have_logs_and_values(self):
        # POINT 11-12
        global page
        page.element_click(MetalsColors.DROP_DOWN_BUTTON_COLORS)
        page.element_click(MetalsColors.DROP_DOWN_YELLOW)
        assert page.find_need_element(MetalsColors.SELECTED_DROP_DOWN_YELLOW), f'{Constants.YELLOW} is not chosen'
        assert page.find_need_element(MetalsColors.LOGS), "Log is not presented"
        assert page.is_text_found(MetalsColors.LOGS, Constants.YELLOW), "Text is not expected"

    def test_select_dropdown_metals_have_logs_and_values(self):
        # POINT 13-14
        global page
        page.element_click(MetalsColors.DROP_DOWN_BUTTON_METALS)
        page.element_click(MetalsColors.DROP_DOWN_GOLD)
        assert page.find_need_element(MetalsColors.SELECTED_DROP_DOWN_GOLD), f'{Constants.GOLD} is not chosen'
        assert page.find_need_element(MetalsColors.LOGS), "Log is not presented"
        assert page.is_text_found(MetalsColors.LOGS, Constants.GOLD), f"Drop down {Constants.GOLD} do not be chosen"

    def test_select_checkboxes_vegetables_have_logs_and_values(self):
        # POINT 15
        global page
        vegetables = [MetalsColors.DROP_DOWN_BUTTON_VEGETABLES,
                      MetalsColors.DROP_DOWN_VEGETABLES,
                      MetalsColors.DROP_DOWN_CUCUMBER,
                      MetalsColors.DROP_DOWN_TOMATO]
        for i in vegetables:
            page.element_click(i)
        assert page.is_element_selected(MetalsColors.SELECTED_DROP_DOWN_CUCUMBER) and page.is_element_selected(
            MetalsColors.SELECTED_DROP_DOWN_TOMATO), 'Elements are not chosen'

    def test_submit_button_and_right_result_logs(self):
        # POINT 16
        global page
        page.element_click(MetalsColors.SUBMIT_BUTTON)
        assert page.is_text_found(MetalsColors.LOGS, 'clicked'), "The button is not clicked"

        expected_log_values = [Constants.WATER + ', ' + Constants.WIND,
                               Constants.YELLOW,
                               Constants.GOLD,
                               "Cucumber, Tomato"]
        # for i in expected_log_values:
        #     assert page.find_need_element((By.XPATH, MetalsColors.LOG_ROW % count)).text.find(i) != -1, f"Element {i}" \
        #                                                                                            f" is not expected"
        #     count += 1
        count = Constants.START_LOG_ROW_INDEX
        for i in expected_log_values:
            assert page.find_need_element((By.XPATH, MetalsColors.LOG_ROW.format(count))).text.find(i) != -1, \
                f"Element {i} is not expected"
            count += 1



















