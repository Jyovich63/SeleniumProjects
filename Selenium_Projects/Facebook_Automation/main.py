from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

def facebook_login(email, password):
    service_obj = Service("C:\\Program Files\\Drivers")
    driver = webdriver.Edge(service=service_obj)
    try:
        # Open Facebook login page
        driver.get("https://www.facebook.com/")

        # Find email and password input fields and fill them
        email_input = driver.find_element(By.ID,"email")
        email_input.send_keys(email)

        password_input = driver.find_element(By.ID,"pass")
        password_input.send_keys(password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        # Wait for the login process to complete
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window
        driver.quit()



facebook_login("mail_id@gmail.com", "password")
