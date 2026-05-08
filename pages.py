import time
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Address
    FROM_FIELD_LOCATOR = (By.ID, "from")
    TO_FIELD_LOCATOR = (By.ID, "to")

    # Selecting Supportive Plan
    SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(@class, 'tcard-title') and text()='Supportive']")

    # Phone Number
    PHONE_NUMBER_FIELD = (By.ID, "phone")
    CONFIRMATION_FIELD = (By.ID, "code")

    # Add a Credit Card
    PAYMENT_METHOD = (By.CLASS_NAME, "pp-button")
    ADD_CARD_BUTTON = (By.CLASS_NAME, "pp-plus")
    CARD_NUMBER_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.XPATH, "//input[@placeholder='12']")
    LINK_BUTTON = (By.XPATH, "//button[contains(text(), 'Link')]")

    # Comment For Driver
    COMMENT_FIELD = (By.ID, "comment")

    # Blanket and Handkerchiefs
    BLANKET_SLIDER = (By.CLASS_NAME, "slider")

    # Ordering 2 Ice Creams
    ICE_CREAM_PLUS_BUTTON = (By.CLASS_NAME, "counter-plus")
    ICE_CREAM_COUNTER = (By.CLASS_NAME, "counter-value")

    # Ordering a Taxi
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")

    # SMS Code confirmation
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirm')]")

    # Payment modal close
    PAYMENT_MODAL_CLOSE = (By.XPATH, "//div[@class='payment-picker open']//div[@class='modal']//button[@class='close-button section-close']")

    # Opens Phone Input Modal
    PHONE_NUMBER_BUTTON = (By.CLASS_NAME, "np-button")

    # Order button
    ORDER_TAXI_BUTTON = (By.CLASS_NAME, "smart-button")

    #Supportive Plan Card
    SUPPORTIVE_PLAN_CARD = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Supportive']]")

    # Address
    FROM_FIELD_LOCATOR = (By.ID, "from")
    TO_FIELD_LOCATOR = (By.ID, "to")

    # Selecting Supportive Plan
    SUPPORTIVE_PLAN = (By.XPATH, "//div[contains(@class, 'tcard-title') and text()='Supportive']")

    # Phone Number
    PHONE_NUMBER_FIELD = (By.ID, "phone")
    CONFIRMATION_FIELD = (By.ID, "code")

    # Add a Credit Card
    PAYMENT_METHOD = (By.CLASS_NAME, "pp-button")
    ADD_CARD_BUTTON = (By.CLASS_NAME, "pp-plus")
    CARD_NUMBER_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.XPATH, "//input[@placeholder='12']")
    LINK_BUTTON = (By.XPATH, "//button[contains(text(), 'Link')]")

    # Comment For Driver
    COMMENT_FIELD = (By.ID, "comment")

    # Blanket and Handkerchiefs
    BLANKET_SLIDER = (By.CLASS_NAME, "slider")

    # Ordering 2 Ice Creams
    ICE_CREAM_PLUS_BUTTON = (By.CLASS_NAME, "counter-plus")
    ICE_CREAM_COUNTER = (By.CLASS_NAME, "counter-value")

    # Ordering a Taxi
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")

    # SMS Code confirmation
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirm')]")

    # Payment modal close
    PAYMENT_MODAL_CLOSE = (By.XPATH,
                           "//div[@class='payment-picker open']//div[@class='modal']//button[@class='close-button section-close']")

    # Opens Phone Input Modal
    PHONE_NUMBER_BUTTON = (By.CLASS_NAME, "np-button")

    # Order button
    ORDER_TAXI_BUTTON = (By.CLASS_NAME, "smart-button")

    # Supportive Plan Card
    SUPPORTIVE_PLAN_CARD = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Supportive']]")

    # Handkerchiefs Checkbox
    HANDKERCHIEFS_CHECKBOX = (By.XPATH, "//input [@class='switch-input']")

    # Methods
    def set_from_address(self, driver, address):
        from_element = self.wait.until(expected_conditions.element_to_be_clickable(self.FROM_FIELD_LOCATOR))
        from_element.clear()
        time.sleep(0.5)
        from_element.send_keys(address)

    def set_to_address(self, driver, address):
        to_element = self.wait.until(expected_conditions.element_to_be_clickable(self.TO_FIELD_LOCATOR))
        to_element.clear()
        time.sleep(0.5)
        to_element.send_keys(address)

    def set_code(self, driver, code):
        driver.find_element(*self.CONFIRMATION_FIELD).send_keys(code)

    def click_payment_method(self, driver):
        payment_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD)
        )
        payment_element.click()
        # Wait a moment for the modal to fully load
        time.sleep(1)

    def click_add_card(self, driver):
        add_card_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CARD_BUTTON)
        )
        add_card_element.click()

    def set_card_number(self, driver, card_number):
        driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_number)

    def set_card_code(self, driver, card_code):
        driver.find_element(*self.CARD_CODE_FIELD).send_keys(card_code)

    def click_link_button(self, driver):
        driver.find_element(*self.LINK_BUTTON).click()

    def set_comment(self, driver, comment):
        driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    def click_blanket_slider(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BLANKET_SLIDER)).click()

    def is_blanket_selected(self):  # Remove driver parameter
        blanket_element = self.driver.find_element(*self.BLANKET_SLIDER)
        return blanket_element.get_property('checked')

    def click_ice_cream_plus_button(self, driver):
        ice_cream_plus = driver.find_element(*self.ICE_CREAM_PLUS_BUTTON)
        ice_cream_plus.click()

    def wait_for_car_search_modal(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "order-body")))

    def get_comment_text(self, driver):
        return driver.find_element(*self.COMMENT_FIELD).get_attribute("value")

    def get_payment_method_text(self, driver):
        payment_element = driver.find_element(*self.PAYMENT_METHOD)
        return payment_element.text

    def set_phone_number(self, driver, phone):
        phone_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.PHONE_NUMBER_FIELD)
        )
        # Try clicking the label instead
        label = driver.find_element(By.CSS_SELECTOR, "label[for='phone']")
        label.click()
        phone_field.send_keys(phone)

    def change_focus_from_code_field(self, driver):
        from selenium.webdriver.common.keys import Keys
        code_field = driver.find_element(*self.CARD_CODE_FIELD)
        code_field.send_keys(Keys.TAB)

    def click_supportive_plan(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUPPORTIVE_PLAN)).click()
        time.sleep(2)

    def set_from(self, address):
        from_field = self.driver.find_element(*self.FROM_FIELD_LOCATOR)
        from_field.clear()

        if from_field.get_attribute("value") != "":
            from_field.clear()  # Try clearing again if needed

        from_field.send_keys(address)

    def set_to(self, address):
        to_field = self.driver.find_element(*self.TO_FIELD_LOCATOR)
        to_field.clear()

        # Verify the field is actually clear
        if to_field.get_attribute("value") != "":
            to_field.clear()  # Try clearing again if needed

        to_field.send_keys(address)

    def get_from(self, driver):
        return driver.find_element(*self.FROM_FIELD_LOCATOR).get_attribute("value")

    def get_to(self, driver):
        return driver.find_element(*self.TO_FIELD_LOCATOR).get_attribute("value")

    def get_ice_cream_counter(self, driver):
        return driver.find_element(*self.ICE_CREAM_COUNTER).text

    def click_call_a_taxi_button(self):
        from_value = self.driver.find_element(*self.FROM_FIELD_LOCATOR).get_attribute("value")
        to_value = self.driver.find_element(*self.TO_FIELD_LOCATOR).get_attribute("value")

        # Add a small wait before clicking
        time.sleep(2)

        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def click_next_button(self, driver):
        driver.find_element(*self.NEXT_BUTTON).click()

    def enter_sms_code(self, driver, code):
        driver.find_element(*self.CONFIRMATION_FIELD).send_keys(code)

    def click_confirm_button(self, driver):
        driver.find_element(*self.CONFIRM_BUTTON).click()

    def close_payment_method_modal(self, driver):
        driver.find_element(*self.PAYMENT_MODAL_CLOSE).click()

    def get_phone_number(self, driver):
        return driver.find_element(*self.PHONE_NUMBER_FIELD).get_attribute("value")

    def is_supportive_plan_selected(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN).text

    def set_sms_code(self, driver, sms_code):
        driver.find_element(*self.CONFIRMATION_FIELD).send_keys(sms_code)

    def click_phone_number_button(self, driver):
        driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def click_order_taxi(self, driver):
        driver.find_element(*self.ORDER_TAXI_BUTTON).click()

    def verify_handkerchief_checkbox_check(self):
        return self.driver.find_element(*self.HANDKERCHIEFS_CHECKBOX).get_attribute("checked")

    def order_ice_creams(self, quantity):
        for i in range(quantity):
            self.click_ice_cream_plus_button(self.driver)