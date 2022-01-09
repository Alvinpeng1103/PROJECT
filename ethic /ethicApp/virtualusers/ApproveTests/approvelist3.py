from selenium import webdriver
import time
import os

# Test to see if sign up hyperlink redirects to register page

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/login/")
time.sleep(1)
driver.find_element_by_name("username").send_keys("ethicscommittee")
time.sleep(1)
driver.find_element_by_name("password").send_keys("qwer1234zxcv")
time.sleep(1)
driver.find_element_by_name("Login").click()
time.sleep(1)
driver.find_element_by_name("Logout").click()
time.sleep(5)
driver.close()
