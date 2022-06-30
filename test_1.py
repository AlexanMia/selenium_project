from .util.locators import Locators
from .util.constants import Constants
from .pages.base_page import BasePage


class Test1:
    def test_open_test_site(self, browser):
        global page
        page = BasePage(browser, Constants.link_1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу

    def test_proper_title(self):
        # POINT 2
        global page
        assert page.get_page_title() == Constants.PAGE_TITLE, f"Title is not {Constants.PAGE_TITLE}"

    def test_logging(self, browser):
        # CHECKED
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

    def test_proper_title(self, browser):
        # CHECKED
        # POINT 5
        global page
        # TODO одна и та же функция дважды, это ничего?
        assert page.get_page_title() == Constants.PAGE_TITLE, f"Title is not {Constants.PAGE_TITLE}"

    def test_is_items_and_propers_text(self, browser):
        # CHECKED
        # POINT 6
        items_locators = [Locators.home,
                          Locators.contact_form,
                          Locators.service,
                          Locators.metalscolours
                          ]
        expected_items_of_main_page = [Constants.PROPER_TEXT_1,
                                       Constants.PROPER_TEXT_2,
                                       Constants.PROPER_TEXT_3,
                                       Constants.PROPER_TEXT_4
                                       ]
        actual_texts_items = []
        [actual_texts_items.append(page.get_elements_text(i)) for i in items_locators]
        assert all([a == b for a, b in zip(actual_texts_items, expected_items_of_main_page)]), 'Texts are not equal'

    def test_is_four_images(self, browser):
        # CHECKED
        # POINT 7
        global page
        images_locators = [Locators.IMAGE_1,
                           Locators.IMAGE_2,
                           Locators.IMAGE_3,
                           Locators.IMAGE_4]
        assert all([page.find_need_element(i) for i in images_locators]), 'Not all elements are showed'

    def test_are_four_texts_under_images(self, browser):
        # CHECKED
        # POINT 8
        global page
        texts_locators = [Locators.TEXT_INCLUDE, Locators.TEXT_FLEXIBLE, Locators.TEXT_MULTIPLATFORM,
                          Locators.TEXT_ALREADY]
        expected_texts = [Constants.TEXT_UNDER_PICT_1, Constants.TEXT_UNDER_PICT_2,
                          Constants.TEXT_UNDER_PICT_3,
                          Constants.TEXT_UNDER_PICT_4]
        actual_texts = []
        [actual_texts.append(page.get_elements_text(i).replace('\n', ' ')) for i in texts_locators]
        assert all([a == b for a, b in zip(actual_texts, expected_texts)]), 'Texts are not equal'

    def test_is_text_of_the_main_headers(self, browser):
        # CHECKED
        # POINT 9
        global page
        texts_of_main_page = {
            page.get_elements_text(Locators.TEXT_of_the_MAIN_PAGE_1): Constants.TEXT_ON_MAIN_PAGE_1,
            page.get_elements_text(Locators.TEXT_of_the_MAIN_PAGE_2): Constants.TEXT_ON_MAIN_PAGE_2
            }
        for i, j in texts_of_main_page.items():
            assert i == j, f'Texts is not equal {i} = {j}'

    def test_is_the_iframe(self, browser):
        # CHECKED
        # POINT 10
        global page
        assert page.find_need_element(Locators.IFRAME), 'Iframe is not be found'

    def test_switch_to_iframe(self, browser):
        # CHECKED
        # POINT 11
        global page
        browser.switch_to.frame('frame')
        assert page.find_need_element(Locators.IFRAME_BUTTON), 'Iframe button is not be found'

    def test_switch_to_original_window(self, browser):
        # CHECKED
        # POINT 12
        global page
        browser.switch_to.default_content()
        assert page.get_elements_text(Locators.TEXT_OF_SUB) == Constants.TEXT_OF_SUB_HEADER, \
            'Exit from frame is unsuccessful'

    def test_proper_text_of_the_header(self, browser):
        # CHECKED
        # POINT 13
        global page
        assert page.get_elements_text(Locators.TEXT_OF_SUB) == Constants.TEXT_OF_SUB_HEADER, \
            'Texts are not equal'

    def test_proper_link(self, browser):
        # CHECKED
        # POINT 14
        global page
        assert page.find_need_element(Locators.TEXT_OF_SUB).get_attribute('href') == Constants.LINK, \
            'Links are not equal'

    def test_is_left_section(self, browser):
        # CHECKED
        # POINT 15
        global page
        assert page.find_need_element(Locators.LEFT_SECTION), 'Left section is not displayed'

    def test_is_footer(self, browser):
        # CHECKED
        # POINT 16
        global page
        assert page.find_need_element(Locators.FOOTER), 'Footer is not displayed'



