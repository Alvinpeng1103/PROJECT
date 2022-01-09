from selenium import webdriver
import time
import os

# Test to see if register function is working

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/register/")
time.sleep(3)
driver.find_element_by_name("first_name").send_keys("example")
time.sleep(3)
driver.find_element_by_name("last_name").send_keys("example")
time.sleep(3)
driver.find_element_by_name("username").send_keys("example")
time.sleep(3)
driver.find_element_by_name("email").send_keys("example@example.com")
time.sleep(3)
driver.find_element_by_name("password1").send_keys("usyd123456")
time.sleep(3)
driver.find_element_by_name("password2").send_keys("usyd123456")
time.sleep(3)
driver.find_element_by_name("Register").click()
time.sleep(3)

# This section deletes the example user so you can run the test again
driver.get("http://localhost:8000/admin/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("admin")
time.sleep(3)
driver.find_element_by_name("password").send_keys("admin")
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'example')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.close()
