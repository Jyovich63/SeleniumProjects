from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
import time


@given('I am on the Facebook login page')
def step_impl(context):
    
    service_obj = Service("C:\\Program Files\\Drivers\\msedgedriver.exe")
    context.driver = webdriver.Edge(service=service_obj)
    context.driver.get("https://www.facebook.com/")

    # Wait for page to load
    time.sleep(2)

@when('I enter my username "{username}"')
def step_impl(context, username):
    email_field = context.driver.find_element(By.ID,"email")
    email_field.send_keys(username)

@when('I enter my password "{password}"')
def step_impl(context, password):
    password_field = context.driver.find_element(By.ID,"pass")
    password_field.send_keys(password)

@when('I click the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.NAME,"login")
    login_button.click()

@then('I should be logged in to my account')
def step_impl(context):
    # Wait for login to complete and page to load
    time.sleep(5)

    # assertions here to check if the login was successful
    assert "Facebook" in context.driver.title

    # Close the browser
    context.driver.quit()
