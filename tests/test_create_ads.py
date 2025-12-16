from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import PersonalData

class TestCreateAds:
    def test_noauthtorized_create_ads(self, driver): 
        add_ads = driver.find_element(*Locators.ADS_BUTTON)
        add_ads.click()

        auth_form = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.AUTH_ADS))
        assert auth_form.is_displayed()


    def test_authtorized_create_ads(self, driver): 
        user_email = PersonalData.user_email 
        user_password = PersonalData.user_password

        login_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        login_button.click()

        input_email = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        input_email.send_keys(user_email)

        input_password = driver.find_element(*Locators.INPUT_PASSWORD)
        input_password.send_keys(user_password)
    
        submit_button = driver.find_element(*Locators.FORM_LOGIN_BUTTON)
        submit_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.USER_AVATAR))

        add_ads = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.ADS_BUTTON))
        add_ads.click()

        title_ads = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INPUT_ADS_TITLE))
        title_ads.send_keys('DeLorean')

        category_button = driver.find_element(*Locators.CATEGORY_BUTTON)
        category_button.click()
    
        choice_category = driver.find_element(*Locators.CHOICE_CATEGORY)
        choice_category.click()

        condition_old = driver.find_element(*Locators.CONDITION_BUTTON_OLD)
        condition_old.click()

        city_button = driver.find_element(*Locators.CITY_BUTTON)
        city_button.click()

        choice_city = driver.find_element(*Locators.CHOICE_CITY)
        choice_city.click()
    
        description_ads = driver.find_element(*Locators.INPUT_ADS_DESCRIPTION)
        description_ads.send_keys('Из фильма "Назад в будущее"')
    
        price_ads = driver.find_element(*Locators.INPUT_ADS_PRICE)
        price_ads.send_keys('100500')

        publish_button = driver.find_element(*Locators.PUBLISH_BUTTON)
        publish_button.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.USER_AVATAR))

        avatar_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.USER_AVATAR))
        avatar_button.click()

        my_ads = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.MY_ADS))
        assert my_ads.is_displayed()
