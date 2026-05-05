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
    from_field_locator = (By.ID, "from")
    to_field_locator = (By.ID, "to")

    # Selecting Supportive Plan
    supportive_plan = (By.XPATH, "//div[contains(@class, 'tcard-title') and text()='Supportive']")

    # Phone Number
    phone_number_field = (By.ID, "phone")
    confirmation_field = (By.ID, "code")

    # Add a Credit Card
    payment_method = (By.CLASS_NAME, "pp-button")
    add_card_button = (By.CLASS_NAME, "pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.XPATH, "//input[@placeholder='12']")
    link_button = (By.XPATH, "//button[contains(text(), 'Link')]")

    # Comment For Driver
    comment_field = (By.ID, "comment")

    # Blanket and Handkerchiefs
    blanket_slider = (By.CLASS_NAME, "slider")

    # Ordering 2 Ice Creams
    ice_cream_plus_button = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter = (By.CLASS_NAME, "counter-value")

    # Ordering a Taxi
    call_taxi_button = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")

    # SMS Code confirmation
    next_button = (By.XPATH, "//button[contains(text(), 'Next')]")
    confirm_button = (By.XPATH, "//button[contains(text(), 'Confirm')]")

    # Payment modal close
    payment_modal_close = (By.XPATH, "//div[@class='payment-picker open']//div[@class='modal']//button[@class='close-button section-close']")

    # Opens Phone Input Modal
    phone_number_button = (By.CLASS_NAME, "np-button")

    # Order button
    order_taxi_button = (By.CLASS_NAME, "smart-button")

    #Supportive Plan Card
    supportive_plan_card = (By.XPATH, "//div[contains(@class, 'tcard') and .//div[text()='Supportive']]")

    # Methods
    def set_from_address(self, driver, address):
        from_element = self.wait.until(expected_conditions.element_to_be_clickable(self.from_field_locator))
        from_element.clear()
        time.sleep(0.5)  # Small pause after clearing
        from_element.send_keys(address)

    def set_to_address(self, driver, address):
        to_element = self.wait.until(expected_conditions.element_to_be_clickable(self.to_field_locator))
        to_element.clear()  # Fixed: now using to_element
        time.sleep(0.5)
        to_element.send_keys(address)

    def set_code(self, driver, code):
        driver.find_element(*self.confirmation_field).send_keys(code)

    def click_payment_method(self, driver):
        payment_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.payment_method)
        )
        payment_element.click()
        # Wait a moment for the modal to fully load
        time.sleep(1)

    def click_add_card(self, driver):
        # Wait for the payment modal to open and the add card button to be clickable
        add_card_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.add_card_button)
        )
        add_card_element.click()

    def set_card_number(self, driver, card_number):
        driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, driver, card_code):
        driver.find_element(*self.card_code_field).send_keys(card_code)

    def click_link_button(self, driver):
        driver.find_element(*self.link_button).click()

    def set_comment(self, driver, comment):
        driver.find_element(*self.comment_field).send_keys(comment)

    def click_blanket_slider(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.blanket_slider)).click()

    def is_blanket_selected(self):  # Remove driver parameter
        blanket_element = self.driver.find_element(*self.blanket_slider)
        return blanket_element.get_property('checked')

    def click_ice_cream_plus_button(self, driver):
        element = driver.find_element(*self.ice_cream_plus_button)
        element.click()

    def wait_for_car_search_modal(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "order-body")))

    def get_comment_text(self, driver):
        return driver.find_element(*self.comment_field).get_attribute("value")

    def get_payment_method_text(self, driver):
        payment_element = driver.find_element(*self.payment_method)
        return payment_element.text

    def set_phone_number(self, driver, phone):
        # Wait for the phone field to be present
        phone_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.phone_number_field)
        )
        # Try clicking the label instead
        label = driver.find_element(By.CSS_SELECTOR, "label[for='phone']")
        label.click()
        phone_field.send_keys(phone)

    def change_focus_from_code_field(self, driver):
        from selenium.webdriver.common.keys import Keys
        code_field = driver.find_element(*self.card_code_field)
        code_field.send_keys(Keys.TAB)

    def click_supportive_plan(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.supportive_plan)).click()

    def set_from(self, address):
        """Set 'from' address with double-clear verification"""
        from_field = self.driver.find_element(*self.from_field_locator)
        from_field.clear()

        # Verify the field is actually clear
        if from_field.get_attribute("value") != "":
            from_field.clear()  # Try clearing again if needed

        from_field.send_keys(address)

    def set_to(self, address):
        """Set 'to' address with double-clear verification"""
        to_field = self.driver.find_element(*self.to_field_locator)
        to_field.clear()

        # Verify the field is actually clear
        if to_field.get_attribute("value") != "":
            to_field.clear()  # Try clearing again if needed

        to_field.send_keys(address)

    def get_from(self, driver):
        return driver.find_element(*self.from_field_locator).get_attribute("value")

    def get_to(self, driver):
        return driver.find_element(*self.to_field_locator).get_attribute("value")

    def get_ice_cream_counter(self, driver):
        return driver.find_element(*self.ice_cream_counter).text

    def click_call_a_taxi_button(self):
        # Add debug prints to see what's happening
        print("About to click Call a taxi button...")

        # Check if addresses are set first
        from_value = self.driver.find_element(*self.from_field_locator).get_attribute("value")
        to_value = self.driver.find_element(*self.to_field_locator).get_attribute("value")
        print(f"From address: '{from_value}'")
        print(f"To address: '{to_value}'")

        # Add a small wait before clicking
        time.sleep(2)

        self.driver.find_element(*self.call_taxi_button).click()
        print("Clicked Call a taxi button")

    def click_next_button(self, driver):
        driver.find_element(*self.next_button).click()

    def enter_sms_code(self, driver, code):
        driver.find_element(*self.confirmation_field).send_keys(code)

    def click_confirm_button(self, driver):
        driver.find_element(*self.confirm_button).click()

    def close_payment_method_modal(self, driver):
        driver.find_element(*self.payment_modal_close).click()

    def get_phone_number(self, driver):
        return driver.find_element(*self.phone_number_field).get_attribute("value")

    def is_supportive_plan_selected(self):
        supportive_plan_element = self.driver.find_element(*self.supportive_plan_card)
        class_attribute = supportive_plan_element.get_attribute("class")
        print(f"Element classes: {class_attribute}")
        return "active" in class_attribute

    def set_sms_code(self, driver, sms_code):
        driver.find_element(*self.confirmation_field).send_keys(sms_code)

    def click_phone_number_button(self, driver):
        driver.find_element(*self.phone_number_button).click()

    def click_order_taxi(self, driver):
        driver.find_element(*self.order_taxi_button).click()