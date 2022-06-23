import pytest
from selenium.webdriver.common.by import By
from .pages.locators import BasePageLocators, MetalsColors
from .pages.global_meaning import GlobalMeaning
from .pages.base_page import BasePage
import time


class Test3:
    def test_open_test_site(self, browser):
        # POINT 1
        global page
        link = "https://jdi-testing.github.io/jdi-light/index.html"
        page = BasePage(browser, link)  # инициализируем Page Object,
        # передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

    def test_proper_title(self):
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

    def test_going_to_metals_colors(self):
        # POINT 5
        global page
        page.element_click(MetalsColors.metalscolours)

    @pytest.mark.parametrize('loc_radiobutton,loc_logs,global_meaning', [
        (MetalsColors.RADIO_5, MetalsColors.LOGS, GlobalMeaning.NUMBER_5),
        (MetalsColors.RADIO_8, MetalsColors.LOGS, GlobalMeaning.NUMBER_8)
    ])
    def test_radiobutton_have_logs_and_values(self, loc_radiobutton, loc_logs, global_meaning):
        # POINT 6, 7
        global page
        page.element_click(loc_radiobutton)
        assert page.search_element_m(loc_logs), "Log is not presented"
        odd_even = "Even" if page.search_element_m(loc_logs).text.find(global_meaning) and int(
            global_meaning) % 2 == 0 else "Odd"
        assert page.search_element_m(loc_logs).text.find(odd_even), f"Number is not {odd_even}"

    def test_summary_result_in_logs(self):
        # POINT 8
        global page
        page.element_click(MetalsColors.CALCULATE_BUTTON)
        time.sleep(5)
        assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
        time.sleep(5)
        assert page.search_element_m(MetalsColors.CALCULATE_BUTTON_RESULTS).text.find(
            GlobalMeaning.SUMMA) != -1, "Summa is not equal"
        time.sleep(5)

    @pytest.mark.parametrize('loc_checkbox,loc_selected_checkbox,loc_logs,global_meaning', [
        (MetalsColors.CHECKBOX_WATER, MetalsColors.CHECKBOX_WATER_sel, MetalsColors.LOGS, GlobalMeaning.WATER),
        (MetalsColors.CHECKBOX_WIND, MetalsColors.CHECKBOX_WIND_sel, MetalsColors.LOGS, GlobalMeaning.WIND)
    ])
    def test_select_checkboxes_have_logs_and_values(self, loc_checkbox, loc_selected_checkbox, loc_logs, global_meaning):
        # POINT 9-10
        global page
        page.element_click(loc_checkbox)
        assert page.is_element_selected(loc_selected_checkbox), 'Checkbox do not be chosen'
        assert page.search_element_m(loc_logs), "Log is not presented"
        assert page.is_text_found(loc_logs, global_meaning) and \
               page.is_text_found(loc_logs, 'true'), "Text is not expected"

    def test_select_dropdown_colors_have_logs_and_values(self):
        # POINT 11-12
        global page
        page.element_click(MetalsColors.DROP_DOWN_BUTTON_COLORS)
        page.element_click(MetalsColors.DROP_DOWN_YELLOW)
        assert page.search_element_m(MetalsColors.DROP_DOWN_YELLOW_SEL), 'Yellow is not chosen'
        assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
        assert page.is_text_found(MetalsColors.LOGS, GlobalMeaning.YELLOW), "Text is not expected"

    def test_select_dropdown_metals_have_logs_and_values(self):
        # POINT 13-14
        global page
        page.element_click(MetalsColors.DROP_DOWN_BUTTON_METALS)
        page.element_click(MetalsColors.DROP_DOWN_GOLD)
        assert page.search_element_m(MetalsColors.DROP_DOWN_GOLD_SEL), 'Gold is not chosen'
        assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
        assert page.is_text_found(MetalsColors.LOGS, GlobalMeaning.GOLD), "Drop down gold do not be chosen"

    def test_select_checkboxes_vegetables_have_logs_and_values(self):
        # POINT 15
        global page
        vegetables = [MetalsColors.DROP_DOWN_BUTTON_VEGETABLES,
                      MetalsColors.DROP_DOWN_VEGETABLES,
                      MetalsColors.DROP_DOWN_CUCUMBER,
                      MetalsColors.DROP_DOWN_TOMATO]
        for i in vegetables:
            page.element_click(i)
        time.sleep(5)
        assert page.is_element_selected(MetalsColors.DROP_DOWN_CUCUMBER_SEL) and page.is_element_selected(
            MetalsColors.DROP_DOWN_TOMATO_SEL), 'Elements are not chosen'

    def test_submit_button_and_right_result_logs(self):
        # POINT 16
        global page
        page.element_click(MetalsColors.SUBMIT_BUTTON)
        assert page.is_text_found(MetalsColors.LOGS, 'clicked'), "The button is not clicked"

        expected_log_values = [GlobalMeaning.WATER + ', ' + GlobalMeaning.WIND,
                               GlobalMeaning.YELLOW,
                               GlobalMeaning.GOLD,
                               "Cucumber, Tomato"]
        # for i in expected_log_values:
        #     assert page.search_element_m((By.XPATH, MetalsColors.LOG_ROW % count)).text.find(i) != -1, f"Element {i}" \
        #                                                                                            f" is not expected"
        #     count += 1
        count = GlobalMeaning.START_LOG_ROW_INDEX
        for i in expected_log_values:
            assert page.search_element_m((By.XPATH, MetalsColors.LOG_ROW.format(count))).text.find(i) != -1, \
                f"Element {i} is not expected"
            count += 1



















