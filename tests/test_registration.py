
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import generate_email
from data import PersonalData


class TestRegistration:
    def test_valid_registration(self, driver):
        email = generate_email()
        user_password = PersonalData.user_password

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        no_account_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.NO_ACC_BUTTON))
        no_account_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(user_password)

        repeat_password = driver.find_element(*Locators.INPUT_REPEAT_PASSWORD)
        repeat_password.send_keys(user_password)
        
        create_account = driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON)
        create_account.click()

        avatar = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.USER_AVATAR))
        assert avatar.is_displayed()

        username = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.USER_NAME))
        assert username.is_displayed()

    def test_invalid_registration(self, driver):
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        no_account_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.NO_ACC_BUTTON))
        no_account_button.click()

        email_input = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        email_input.send_keys("pochta")

        create_account = driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON)
        create_account.click()

        error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ERROR_EMAIL))
        assert error_message.is_displayed()

    def test_olduser_registration(self, driver):
        user_email = PersonalData.user_email
        user_password = PersonalData.user_password

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        no_account_button = driver.find_element(*Locators.NO_ACC_BUTTON)
        no_account_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(user_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(user_password)

        confirm_password = driver.find_element(*Locators.INPUT_REPEAT_PASSWORD)
        confirm_password.send_keys(user_password)

        create_account = driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON)
        create_account.click()

        error_message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ERROR_EMAIL))
        assert error_message.is_displayed()


