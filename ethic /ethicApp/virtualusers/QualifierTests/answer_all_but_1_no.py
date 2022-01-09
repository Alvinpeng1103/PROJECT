from selenium import webdriver
import time
import os

# Test to see if login is working. Should redurect to managelist page

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/login/")
time.sleep(5)
driver.find_element_by_name("username").send_keys("profile_test")
time.sleep(5)
driver.find_element_by_name("password").send_keys("murkyred49")
time.sleep(5)
driver.find_element_by_name("Login").click()
time.sleep(5)

driver.find_element_by_class_name("start_new_app_button").click()
time.sleep(5)
driver.find_element_by_name("next").click()
time.sleep(5)


driver.find_element_by_id("201no").click() 
driver.find_element_by_id("202no").click()
driver.find_element_by_id("203no").click() 
driver.find_element_by_id("204no").click()
driver.find_element_by_id("205no").click() 
driver.find_element_by_id("206no").click()
driver.find_element_by_id("207no").click() 
driver.find_element_by_id("208no").click()
driver.find_element_by_id("209no").click()
driver.find_element_by_id("210no").click() 
driver.find_element_by_id("211no").click()
driver.find_element_by_id("212no").click()
driver.find_element_by_id("213no").click()
driver.find_element_by_id("214no").click()
driver.find_element_by_id("215no").click()
driver.find_element_by_id("216no").click()
driver.find_element_by_id("217no").click()
driver.find_element_by_id("218no").click()
driver.find_element_by_id("219yes").click()



time.sleep(5)
driver.find_element_by_name("submit").click()
time.sleep(5)

driver.close()