import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .pages.locators import BasePageLocators, MetalsColors, DifferentElements
from .pages.global_meaning import GlobalMeaning
from .pages.base_page import BasePage
import time

from selenium.webdriver.support.select import Select


@pytest.mark.test2
def test_2(browser):
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


    # POINT 5
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

    # POINT 6
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



    # POINT 7
    page.element_click(BasePageLocators.service)
    page.element_click(BasePageLocators.DIFFERENT_ELEMENTS_UNDER_SERVICE)

    # POINT 8
    needed_elements = {GlobalMeaning.NUMBERS_OF_CHECKBOXES: page.find_elements_all(DifferentElements.CHECKBOXES),
                       GlobalMeaning.NUMBERS_OF_RADIOS: page.find_elements_all(DifferentElements.RADIOS),
                       GlobalMeaning.NUMBERS_OF_DROP_DOWN: page.find_elements_all(DifferentElements.DROP_DOWN),
                       GlobalMeaning.NUMBERS_OF_BUTTONS: [page.find_elements_all(DifferentElements.BUTTON_1),
                                                          page.find_elements_all(DifferentElements.BUTTON_2)]}


    for i, j in needed_elements.items():
        # print(len(j))
        assert i == int(len(j)), 'Number of elements do not equal'

    # POINT 9
    assert page.search_element_m(DifferentElements.RIGHT_SECTION), 'Right section is not displayed'

    # POINT 10
    assert page.search_element_m(DifferentElements.LEFT_SECTION), 'Left section is not displayed'

    # POINT 11 b 12
    # два параметра вода и ветер
    page.element_click(DifferentElements.CHECKBOX_WATER)
    assert page.search_element_m(DifferentElements.LOGS), 'Log is not presented'
    assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.WATER) and \
           page.is_text_found(DifferentElements.LOGS, 'true'), 'Text is not expected'

    page.element_click(DifferentElements.CHECKBOX_WIND)
    assert page.search_element_m(DifferentElements.LOGS), "Log is not presented"
    assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.WIND) and \
           page.is_text_found(DifferentElements.LOGS, 'true'), 'Text is not expected'
    selected_checkboxes = {page.is_element_selected(DifferentElements.CHECKBOX_WATER),
                           page.is_element_selected(DifferentElements.CHECKBOX_WIND)
                           }

    for i in selected_checkboxes:
        assert i, 'Checkboxes do not be choose or choose only one'

    # POINT 13 и 14
    page.element_click(DifferentElements.RADIO_SELEN)
    assert page.is_element_selected(DifferentElements.RADIO_SELEN), 'Radio does not be chosen'
    assert page.search_element_m(DifferentElements.LOGS), 'Log is not presented'
    assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.SELEN), 'Text is not expected'

    # POINT 15 и 16
    page.element_click(DifferentElements.DROP_DOWN_YELLOW)
    assert page.is_element_selected(DifferentElements.DROP_DOWN_YELLOW), 'Drop down yellow does not be chosen'
    assert page.search_element_m(DifferentElements.LOGS), "Log is not presented"
    assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.YELLOW), 'Text is not expected'




    # ПАРАМЕТРИЗОВАТЬ
    # POINT 17 и 18
    # два параметра чекбокс вода и ветер

    page.element_click(DifferentElements.CHECKBOX_WATER)
    time.sleep(5)
    assert not page.is_element_selected(DifferentElements.CHECKBOX_WATER), 'Checkbox is chosen'
    assert page.search_element_m(DifferentElements.LOGS), "Log is not presented"
    assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.WATER) and \
           page.is_text_found(DifferentElements.LOGS, 'false'), 'Text is not expected'


    page.element_click(DifferentElements.CHECKBOX_WIND)
    assert not page.is_element_selected(DifferentElements.CHECKBOX_WIND), 'Checkbox is chosen'

    assert page.search_element_m(DifferentElements.LOGS), "Log is not presented"
    assert page.is_text_found(DifferentElements.LOGS, GlobalMeaning.WIND) and \
           page.is_text_found(DifferentElements.LOGS, 'false'), 'Text is not expected'
