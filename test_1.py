from .test_base import TestBase
from .util.locators import MainPage
from .util.constants import Constants


class Test1(TestBase):
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

    def test_proper_title(self, browser):
         # POINT 5
         super().check_title()

    def test_is_items_and_propers_text(self, browser):
        # POINT 6
        items_locators = [MainPage.home,
                          MainPage.contact_form,
                          MainPage.service,
                          MainPage.metalscolours
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
        # POINT 7
        global page
        images_locators = [MainPage.IMAGE_PRACTISE,
                           MainPage.IMAGE_CUSTOM,
                           MainPage.IMAGE_MULTI,
                           MainPage.IMAGE_BASE]
        assert all([page.find_need_element(i) for i in images_locators]), 'Not all elements are showed'

    def test_are_four_texts_under_images(self, browser):
        # POINT 8
        global page
        texts_locators = [MainPage.TEXT_INCLUDE, MainPage.TEXT_FLEXIBLE, MainPage.TEXT_MULTIPLATFORM,
                          MainPage.TEXT_ALREADY]
        expected_texts = [Constants.TEXT_UNDER_PICT_1, Constants.TEXT_UNDER_PICT_2,
                          Constants.TEXT_UNDER_PICT_3,
                          Constants.TEXT_UNDER_PICT_4]
        actual_texts = []
        [actual_texts.append(page.get_elements_text(i).replace('\n', ' ')) for i in texts_locators]
        assert all([a == b for a, b in zip(actual_texts, expected_texts)]), 'Texts are not equal'

    def test_is_text_of_the_main_headers(self, browser):
        # POINT 9
        global page
        texts_of_main_page = {
            page.get_elements_text(MainPage.TEXT_OF_THE_MAIN_PAGE_TITLE): Constants.TEXT_ON_MAIN_PAGE_1,
            page.get_elements_text(MainPage.TEXT_OF_THE_MAIN_PAGE_TXT): Constants.TEXT_ON_MAIN_PAGE_2
            }
        for i, j in texts_of_main_page.items():
            assert i == j, f'Texts is not equal {i} = {j}'

    def test_is_the_iframe(self, browser):
        # POINT 10
        global page
        assert page.find_need_element(MainPage.IFRAME), 'Iframe is not be found'

    def test_switch_to_iframe(self, browser):
        # POINT 11
        global page
        browser.switch_to.frame('frame')
        assert page.find_need_element(MainPage.IFRAME_BUTTON), 'Iframe button is not be found'

    def test_switch_to_original_window(self, browser):
        # POINT 12
        global page
        browser.switch_to.default_content()
        assert page.get_elements_text(MainPage.TEXT_OF_SUB) == Constants.TEXT_OF_SUB_HEADER, \
            'Exit from frame is unsuccessful'

    def test_proper_text_of_the_header(self, browser):
        # POINT 13
        global page
        assert page.get_elements_text(MainPage.TEXT_OF_SUB) == Constants.TEXT_OF_SUB_HEADER, \
            'Texts are not equal'

    def test_proper_link(self, browser):
        # POINT 14
        global page
        assert page.find_need_element(MainPage.TEXT_OF_SUB).get_attribute('href') == Constants.LINK, \
            'Links are not equal'

    def test_is_left_section(self, browser):
        # POINT 15
        global page
        assert page.find_need_element(MainPage.LEFT_SECTION), 'Left section is not displayed'

    def test_is_footer(self, browser):
        # POINT 16
        global page
        assert page.find_need_element(MainPage.FOOTER), 'Footer is not displayed'



