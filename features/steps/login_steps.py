
import time
import allure
from behave import given, when, then
from pages.login_page import LoginPage
from config import ZEN_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD


@given("I navigate to Zen Portal")
@allure.step("Navigate to Zen Portal")
def step_open_zen_portal(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_portal(ZEN_URL)


@then("I validate username and password input boxes")
@allure.step("Validate username and password input boxes")
def step_validate_input_boxes(context):
    context.login_page.validate_input_boxes()


@then("I validate submit button is working")
@allure.step("Validate submit button")
def step_validate_submit_button(context):
    context.login_page.validate_submit_button()


@when("I login with valid username and password")
@allure.step("Login with valid username and password")
def step_valid_login(context):
    context.login_page.login(VALID_USERNAME, VALID_PASSWORD)
    time.sleep(5)


@when("I login with invalid username and password")
@allure.step("Login with invalid username and password")
def step_invalid_login(context):
    context.login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    time.sleep(3)


@then("I should be logged in successfully")
@allure.step("Verify successful login")
def step_verify_successful_login(context):
    context.login_page.close_popup_if_visible()
    assert "login" not in context.driver.current_url.lower()


@then("I should not be logged in successfully")
@allure.step("Verify unsuccessful login")
def step_verify_unsuccessful_login(context):
    assert "login" in context.driver.current_url.lower()


@then("I logout from Zen Portal")
@allure.step("Logout from Zen Portal")
def step_logout(context):
    context.login_page.logout()