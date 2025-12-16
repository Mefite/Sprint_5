from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import PersonalData


class TestLogin:
    def test_login(self, driver):
        user_email = PersonalData.user_email 
        user_password = PersonalData.user_password
      
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(user_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(user_password)
    
        submit_button = driver.find_element(*Locators.FORM_LOGIN_BUTTON)
        submit_button.click()

        avatar = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.USER_AVATAR))
        assert avatar.is_displayed()

        username = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.USER_NAME))
        assert username.is_displayed()
        