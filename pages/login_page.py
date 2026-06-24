
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.username = (By.XPATH, "//label[contains(text(),'Email')]/following::input[1]")
        self.password = (By.XPATH, "//label[contains(text(),'Password')]/following::input[1]")
        self.submit_btn = (By.XPATH, "//button[contains(text(),'Sign in')]")

        self.close_popup_btn = (By.CSS_SELECTOR, "button.custom-close-button")
        self.profile_menu = (By.CSS_SELECTOR, ".user-name-div")
        self.logout_btn = (
            By.XPATH,
            "//*[contains(@class,'user-avatar-menu') and contains(.,'Log out')]"
        )

    def open_portal(self, url):
        self.driver.get(url)

    def validate_input_boxes(self):
        try:
            username_box = self.wait.until(
                EC.visibility_of_element_located(self.username)
            )
            password_box = self.wait.until(
                EC.visibility_of_element_located(self.password)
            )

            assert username_box.is_displayed()
            assert password_box.is_displayed()

        except TimeoutException:
            raise Exception("Username or Password input box not visible")

    def validate_submit_button(self):
        try:
            button = self.wait.until(
                EC.visibility_of_element_located(self.submit_btn)
            )

            assert button.is_displayed()
            assert button.is_enabled()

        except TimeoutException:
            raise Exception("Submit button not visible or not enabled")

    def login(self, username, password):
        try:
            username_box = self.wait.until(
                EC.visibility_of_element_located(self.username)
            )
            password_box = self.wait.until(
                EC.visibility_of_element_located(self.password)
            )

            username_box.clear()
            username_box.send_keys(username)

            password_box.clear()
            password_box.send_keys(password)

            self.wait.until(
                EC.element_to_be_clickable(self.submit_btn)
            ).click()

        except TimeoutException:
            raise Exception("Login elements not found within timeout")

        except NoSuchElementException:
            raise Exception("Login element not found")

    def close_popup_if_visible(self):
        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.close_popup_btn)
            )
            close_button.click()

        except:
            pass

    def logout(self):
        try:
            self.close_popup_if_visible()

            profile = self.wait.until(
                EC.element_to_be_clickable(self.profile_menu)
            )
            profile.click()

            logout_button = self.wait.until(
                EC.element_to_be_clickable(self.logout_btn)
            )
            logout_button.click()

        except TimeoutException:
            raise Exception("Logout button not found")