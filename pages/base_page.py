# base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать
from selenium.webdriver.common.by import By

from .locators import BasePageLocators, BasketPageLocators, GlobalMeaning, DifferentElements, MetalsColors

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_definite_title(self):
        return self.browser.title

    def element_click(self, locator):
        return self.find_element_1(locator).click()

    def find_element_1(self, locator):
        return self.browser.find_element(*locator)


    def search_element_m(self, locator):
        return self.find_element_1(locator)

    def find_elements_all(self, locator):
        return self.browser.find_elements(*locator)

    def is_element_selected(self, locator):
        return self.find_element_1(locator).is_selected()

    def enter_value_into_box(self, locator, meaning):
        return self.find_element_1(locator).send_keys(meaning)

    def get_elements_text(self, locator):
        return self.find_element_1(locator).text

    # написать метод где сравнение с -1
    def is_text_found(self, locator, text):
        return self.get_elements_text(locator).find(text) != -1























































