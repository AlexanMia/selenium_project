import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .pages.locators import BasePageLocators, MetalsColors
from .pages.global_meaning import GlobalMeaning
from .pages.base_page import BasePage
import time

from selenium.webdriver.support.select import Select


# ПЕРЕДЕЛАТЬ ВСЕ ФУНКЦИИ ДЛЯ ТЕСТ1 И ТЕСТ2




@pytest.mark.test3
def test_3(browser):
    link = "https://jdi-testing.github.io/jdi-light/index.html"
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    assert page.should_be_definite_title() == "Home Page", "Title is not Home Page"

    page.element_click(BasePageLocators.LOGIN)
    page.enter_value_into_box(BasePageLocators.LOG, GlobalMeaning.user_name)
    page.enter_value_into_box(BasePageLocators.PASSWORD, GlobalMeaning.password)
    page.element_click(BasePageLocators.BUTTON_ENTER)
    assert page.find_element_1(BasePageLocators.NAME_USER).text == GlobalMeaning.NAME_USER, \
        f"User's name is not {GlobalMeaning.NAME_USER}"

    page.element_click(MetalsColors.metalscolours)

    # ПАРАМЕТРИЗОВАТЬ

    page.element_click(MetalsColors.RADIO_5)
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    odd_even = "Even" if page.search_element_m(MetalsColors.LOGS).text.find(GlobalMeaning.NUMBER_5) and int(
        GlobalMeaning.NUMBER_5) % 2 == 0 else "Odd"
    assert page.search_element_m(MetalsColors.LOGS).text.find(odd_even), f"Number is not {odd_even}"

    page.element_click(MetalsColors.RADIO_8)
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    odd_even = "Even" if page.search_element_m(MetalsColors.LOGS).text.find(GlobalMeaning.NUMBER_8) and int(
        GlobalMeaning.NUMBER_8) % 2 == 0 else "Odd"
    assert page.search_element_m(MetalsColors.LOGS).text.find(odd_even), f"Number is not {odd_even}"

    page.element_click(MetalsColors.CALCULATE_BUTTON)
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    time.sleep(5)
    assert page.search_element_m(MetalsColors.CALCULATE_BUTTON_RESULTS).text.find(GlobalMeaning.SUMMA) != -1, "Summa is not equal"
    time.sleep(5)


    # ПАРАМЕТРИЗОВАТЬ
    page.element_click(MetalsColors.CHECKBOX_WATER)
    assert page.is_element_selected(MetalsColors.CHECKBOX_WATER_sel), 'Checkbox do not be chosen'
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    assert page.is_text_found(MetalsColors.LOGS, GlobalMeaning.WATER) and \
           page.is_text_found(MetalsColors.LOGS, 'true'), "Text is not expected"

    page.element_click(MetalsColors.CHECKBOX_WIND)
    assert page.is_element_selected(MetalsColors.CHECKBOX_WIND_sel), 'Checkbox do not be chosen'
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    assert page.is_text_found(MetalsColors.LOGS, GlobalMeaning.WIND) and \
           page.is_text_found(MetalsColors.LOGS, 'true'), "Text is not expected"

    page.element_click(MetalsColors.DROP_DOWN_BUTTON_COLORS)
    page.element_click(MetalsColors.DROP_DOWN_YELLOW)
    assert page.search_element_m(MetalsColors.DROP_DOWN_YELLOW_SEL), 'Yellow is not chosen'
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    assert page.is_text_found(MetalsColors.LOGS, GlobalMeaning.YELLOW), "Text is not expected"

    page.element_click(MetalsColors. DROP_DOWN_BUTTON_METALS)
    page.element_click(MetalsColors.DROP_DOWN_GOLD)
    assert page.search_element_m(MetalsColors.DROP_DOWN_GOLD_SEL), 'Gold is not chosen'
    assert page.search_element_m(MetalsColors.LOGS), "Log is not presented"
    assert page.is_text_found(MetalsColors.LOGS, GlobalMeaning.GOLD), "Drop down gold do not be chosen"

    vegetables = [MetalsColors.DROP_DOWN_BUTTON_VEGETABLES,
                  MetalsColors.DROP_DOWN_VEGETABLES,
                  MetalsColors.DROP_DOWN_CUCUMBER,
                  MetalsColors.DROP_DOWN_TOMATO]
    for i in vegetables:
        page.element_click(i)
    time.sleep(5)
    assert page.is_element_selected(MetalsColors.DROP_DOWN_CUCUMBER_SEL) and page.is_element_selected(
        MetalsColors.DROP_DOWN_TOMATO_SEL), 'Elements are not chosen'

    page.element_click(MetalsColors.SUBMIT_BUTTON)
    assert page.is_text_found(MetalsColors.LOGS, 'clicked'), "The button is not clicked"

    expected_log_values = [GlobalMeaning.WATER+', '+GlobalMeaning.WIND,
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























