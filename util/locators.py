from selenium.webdriver.common.by import By
from util.constants import Constants


class Locators:
    LOGIN = (By.CSS_SELECTOR, "#user-icon")
    LOG = (By.CSS_SELECTOR, "#name")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_ENTER = (By.CSS_SELECTOR, "#login-button")
    NAME_USER = (By.CSS_SELECTOR, "#user-name")

    home = (By.XPATH, "//a[text()='Home']")

    contact_form = (By.XPATH, '//a[text()="Contact form"]')
    service = (By.CLASS_NAME, "dropdown-toggle")
    metalscolours = (By.XPATH, '//a[text()="Metals & Colors"]')

    IMAGE_1 = (By.CLASS_NAME, "icon-practise")
    IMAGE_2 = (By.CLASS_NAME, "icon-custom")
    IMAGE_3 = (By.CLASS_NAME, "icon-multi")
    IMAGE_4 = (By.CLASS_NAME, "icon-base")

    TEXT_INCLUDE = (By.CLASS_NAME, "benefit-txt")
    TEXTS_PATTERN = '//span[@class="benefit-txt" and contains(text(),"{}")]'
    TEXT_FLEXIBLE = (By.XPATH, TEXTS_PATTERN.format("flexible"))
    TEXT_MULTIPLATFORM = (By.XPATH, TEXTS_PATTERN.format("multiplatform"))
    TEXT_ALREADY = (By.XPATH, TEXTS_PATTERN.format("Already"))

    TEXT_of_the_MAIN_PAGE_1 = (By.CLASS_NAME, "main-title")
    TEXT_of_the_MAIN_PAGE_2 = (By.CLASS_NAME, "main-txt")

    TEXT_OF_SUB = (By.XPATH, '//a[@ui="link" and contains(text(),"JDI")]')

    LEFT_SECTION = (By.CSS_SELECTOR, "#mCSB_1")

    FOOTER = (By.CLASS_NAME, "footer-bg")

    UNDER_SERVICE_BAR_PATTERN = '//a[text()="{}"]'
    SUPPORT_UNDER_SERVICE = (By.XPATH, UNDER_SERVICE_BAR_PATTERN.format("Support"))
    DATES_UNDER_SERVICE = (By.XPATH, UNDER_SERVICE_BAR_PATTERN.format("Dates"))
    COMPLEX_TABLE_UNDER_SERVICE = (By.XPATH, UNDER_SERVICE_BAR_PATTERN.format("Complex Table "))
    SIMPLE_TABLE_UNDER_SERVICE = (By.XPATH, UNDER_SERVICE_BAR_PATTERN.format("Simple Table "))
    TABLE_WITH_PAGES_UNDER_SERVICE = (By.XPATH, UNDER_SERVICE_BAR_PATTERN.format("Table with pages"))
    DIFFERENT_ELEMENTS_UNDER_SERVICE = (By.XPATH, UNDER_SERVICE_BAR_PATTERN.format("Different elements"))

    LEFT_SIDE_BAR_LOCATOR_PATTERN = '//span[contains(text(),"{}")]'
    SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Service"))
    SUPPORT_SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Support"))
    DATES_SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Dates"))
    COMPLEX_TABLE_SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Complex Table "))
    SIMPLE_TABLE_SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Simple Table"))
    TABLE_WITH_PAGES_SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Table with pages"))
    DIFFERENT_ELEMENTS_SERVICE_ON_THE_LEFT = (By.XPATH, LEFT_SIDE_BAR_LOCATOR_PATTERN.format("Different elements"))

    IFRAME = (By.CSS_SELECTOR, "#frame")
    IFRAME_BUTTON = (By.CSS_SELECTOR, "#frame-button")


class DifferentElements:
    CHECKBOXES = (By.CLASS_NAME, "label-checkbox")
    RADIOS = (By.CLASS_NAME, "label-radio")
    DROP_DOWN = (By.XPATH, '//select[@class="uui-form-element"]')
    BUTTON_1 = (By.XPATH, '//button[@class="uui-button" and contains(text(),"Default")]')
    BUTTON_2 = (By.XPATH, '//input[@class="uui-button"]')

    RIGHT_SECTION = (By.CSS_SELECTOR, "#mCSB_2")
    LEFT_SECTION = (By.CSS_SELECTOR, "#mCSB_1")

    CHECKBOX_WATER = (By.XPATH, '//label[@class="label-checkbox"][1]//input')
    SELECTED_CHECKBOX_WATER = (By.XPATH, '//label[@class="label-checkbox"][1]//input[@type="checkbox"]')

    CHECKBOX_WIND = (By.XPATH, '//label[@class="label-checkbox"][3]//input')

    LOGS = (By.XPATH, '//ul[@class="panel-body-list logs"]/child::li')

    RADIO_SELEN = (By.XPATH, '//label[@class="label-radio"][4]//input')

    DROP_DOWN_YELLOW = (By.XPATH, '//select[@class="uui-form-element"]//option[text()="Yellow"]')


class MetalsColors:
    metalscolours = (By.XPATH, '//span[contains(text(),"Metals & Colors")]')
    RADIO_5 = (By.XPATH, f'//p[@class="radio"]//label[text()={Constants.NUMBER_5}]')
    SELECTED_RADIO_5 = (By.XPATH, '//p[@class="radio"]//input[@id="p3"]')

    RADIO_8 = (By.XPATH, f'//p[@class="radio"]//label[text()={Constants.NUMBER_8}]')
    SELECTED_RADIO_8 = (By.XPATH, '//p[@class="radio"]//input[@id="p8"]')

    CALCULATE_BUTTON = (By.XPATH, '//button[@id="calculate-button"]')

    CALCULATE_BUTTON_RESULTS = (By.XPATH, '//li[@class="summ-res"]')

    CHECKBOX_WATER = (By.XPATH, f'//p[@class="checkbox"]//label[text()="{Constants.WATER}"]')
    SELECTED_CHECKBOX_WATER = (By.XPATH, '//p[@class="checkbox"]//input[@id="g1"]')

    CHECKBOX_WIND = (By.XPATH, f'//p[@class="checkbox"]//label[text()="{Constants.WIND}"]')
    SELECTED_CHECKBOX_WIND = (By.XPATH, '//p[@class="checkbox"]//input[@id="g3"]')

    LOGS = (By.XPATH, '//ul[@class="panel-body-list logs"]/child::li')

    DROP_DOWN_BUTTON_COLORS = (By.XPATH, '//button[@title="Colors"]')
    DROP_DOWN_YELLOW = (By.XPATH, '//li[@rel="4"]')
    SELECTED_DROP_DOWN_YELLOW = (By.XPATH, '//li[@class="selected"]')

    DROP_DOWN_BUTTON_METALS = (By.XPATH, '//button[@title="Metals"]//span[@class="caret"]')
    DROP_DOWN_GOLD = (By.XPATH, f'//span[@class="text" and text()="{Constants.GOLD}"]')
    SELECTED_DROP_DOWN_GOLD = (By.XPATH, f'//span[text()="{Constants.GOLD}"]')

    DROP_DOWN_BUTTON_VEGETABLES = (By.XPATH, '//div[@id="salad-dropdown"]')
    DROP_DOWN_VEGETABLES = (By.XPATH, '//label[@for="g7"]')
    DROP_DOWN_CUCUMBER = (By.XPATH, '//label[@for="g5"]')
    SELECTED_DROP_DOWN_CUCUMBER = (By.XPATH, '//input[@id="g5"]')
    DROP_DOWN_TOMATO = (By.XPATH, '//label[@for="g6"]')
    SELECTED_DROP_DOWN_TOMATO = (By.XPATH, '//input[@id="g6"]')

    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit-button"]')

    LOG_ROW = '//ul[@class="panel-body-list results"]//li[{}]'




























class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")


class BasketPageLocators():
    BUTTON_BASKET_page = (By.CSS_SELECTOR, "span.btn-group")

    NOTE_ABOUT_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
    #NOTE_ABOUT_BASKET = ((By.XPATH, "//p[contains(text(), 'empty')]"))
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")





#id content_inner - надпись корзина пуста