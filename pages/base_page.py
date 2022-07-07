# base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_page_title(self):
        return self.browser.title

    def element_click(self, locator):
        return self.find_need_element(locator).click()

    def find_need_element(self, locator):
        return self.browser.find_element(*locator)

    def find_elements_all(self, locator):
        return self.browser.find_elements(*locator)

    def is_element_selected(self, locator):
        return self.find_need_element(locator).is_selected()

    def enter_value_into_box(self, locator, meaning):
        return self.find_need_element(locator).send_keys(meaning)

    def get_elements_text(self, locator):
        return self.find_need_element(locator).text

    def is_text_found(self, locator, text):
        return self.get_elements_text(locator).find(text) != -1























































