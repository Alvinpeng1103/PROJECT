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
time.sleep(5)
driver.find_element_by_name("username").send_keys("normaluser")
time.sleep(5)
driver.find_element_by_name("password").send_keys("qwer1234zxcv")
time.sleep(5)
driver.find_element_by_name("Login").click()
time.sleep(5)
driver.find_element_by_name("start").click()
time.sleep(5)
driver.get("http://localhost:8000/qualifier/success/")
time.sleep(5)
driver.find_element_by_name("next").click()
time.sleep(5)
driver.find_element_by_name("PIS").click()
time.sleep(5)
driver.find_element_by_name("PIS_create").click()
time.sleep(5)
driver.find_element_by_name("submit").click()
time.sleep(5)
driver.close()