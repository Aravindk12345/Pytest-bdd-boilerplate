import pytest

from pytest_bdd import scenarios, given, when, then, parsers, scenario
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test.Constants.constantFields import *
import time


# Scenario

@scenario('../features/login.feature', '1. Verify if the error message is displayed when user gives wrong username',
            example_converters=dict(Username=str, Password=str))

@pytest.mark.usefixtures("setup")
def test_Login_check():
    pass

# Given Steps

@given('User is providing valid URL')
def gloheal_home(browser):
    browser.get(Env_var)
    browser.maximize_window()

@given('User is providing valid <Username>')
def enter_valid_email(Username, browser):
    enter_email = browser.find_element_by_id('identifierId')
    enter_email.click()
    enter_email.send_keys(Username)

@given('User is providing valid <Password>')
def enter_valid_password(Password, browser):
    enter_password = browser.find_element_by_xpath('//input[@type="password"]')
    enter_password.click()
    enter_password.send_keys(Password)

@given('Clicks the next button')
def click_next(browser):
    enter_email = browser.find_element_by_class_name('CwaK9')
    enter_email.click()
    time.sleep(5)

@then('click on next button')
def click_password_next(browser):
    enter_email = browser.find_element_by_class_name('CwaK9')
    enter_email.click()