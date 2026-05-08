from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import data
import helpers
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Check if URL is reachable and navigate to it
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            cls.driver.get(data.URBAN_ROUTES_URL)

        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)
        routes_page.click_call_a_taxi_button()
        assert routes_page.get_from(self.driver) == data.ADDRESS_FROM
        assert routes_page.get_to(self.driver) == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)  # Changed
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)  # Changed
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()
        assert routes_page.is_supportive_plan_selected() == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()

        # Click the phone number button to open the phone input modal
        routes_page.click_phone_number_button(self.driver)

        # Enter phone number
        routes_page.set_phone_number(self.driver, data.PHONE_NUMBER)

        # Click Next to request SMS
        routes_page.click_next_button(self.driver)

        # Get the SMS code from helpers
        code = helpers.retrieve_phone_code(self.driver)

        # Enter the SMS code
        routes_page.enter_sms_code(self.driver, code)

        # Click Confirm to validate
        routes_page.click_confirm_button(self.driver)

        # Assert phone number was entered correctly
        assert routes_page.get_phone_number(self.driver) == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()

        # Add card
        routes_page.click_payment_method(self.driver)
        routes_page.click_add_card(self.driver)
        routes_page.set_card_number(self.driver, data.CARD_NUMBER)
        routes_page.set_card_code(self.driver, data.CARD_CODE)

        # Change focus and link card
        routes_page.change_focus_from_code_field(self.driver)
        routes_page.click_link_button(self.driver)

        #Close modal
        routes_page.close_payment_method_modal(self.driver)

        # Assert card was added
        payment_text = routes_page.get_payment_method_text(self.driver)
        assert "Card" in payment_text

    def test_set_comment(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)

        # Steps 1-4: Set addresses and navigate
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()

        # Step 5: Set the comment using your method and data
        routes_page.set_comment(self.driver, data.MESSAGE_FOR_DRIVER)

        # Step 6: Assert the comment was stored correctly
        stored_comment = routes_page.get_comment_text(self.driver)
        assert stored_comment == data.MESSAGE_FOR_DRIVER

    def test_ordering_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        # Set up addresses
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)

        # Call taxi and select supportive plan
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()

        # Click the blanket and handkerchiefs slider
        routes_page.click_blanket_slider()

        assert routes_page.verify_handkerchief_checkbox_check()

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.order_ice_creams(2)
        assert routes_page.get_ice_cream_counter(self.driver) == "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from_address(self.driver, data.ADDRESS_FROM)
        routes_page.set_to_address(self.driver, data.ADDRESS_TO)
        routes_page.click_call_a_taxi_button()
        routes_page.click_supportive_plan()
        routes_page.click_phone_number_button(self.driver)
        routes_page.set_phone_number(self.driver, data.PHONE_NUMBER)
        routes_page.click_next_button(self.driver)
        code = helpers.retrieve_phone_code(self.driver)  # Get the SMS code
        routes_page.enter_sms_code(self.driver, code)  # Pass it to your method
        routes_page.click_confirm_button(self.driver)
        routes_page.click_payment_method(self.driver)
        routes_page.click_add_card(self.driver)
        routes_page.set_card_number(self.driver, data.CARD_NUMBER)
        routes_page.set_card_code(self.driver, data.CARD_CODE)
        routes_page.click_link_button(self.driver)
        routes_page.close_payment_method_modal(self.driver)
        routes_page.set_comment(self.driver, data.MESSAGE_FOR_DRIVER)
        routes_page.click_order_taxi(self.driver)
        assert routes_page.wait_for_car_search_modal(self.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()