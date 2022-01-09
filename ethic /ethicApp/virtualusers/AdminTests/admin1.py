from selenium import webdriver
import time
import os


# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(30)


# Test to add user
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
driver.find_element_by_xpath("//*[contains(text(), 'Add user')]").click()
time.sleep(3)
driver.find_element_by_name("username").send_keys("example")
time.sleep(3)
driver.find_element_by_name("password1").send_keys("usyd323456")
time.sleep(3)
driver.find_element_by_name("password2").send_keys("usyd323456")
time.sleep(3)
driver.find_element_by_name("_save").click()
time.sleep(3)


#  Test to modify user
driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'example')]").click()
time.sleep(3)
driver.find_element_by_name("first_name").send_keys("example_name")
time.sleep(3)
driver.find_element_by_name("_continue").click()
time.sleep(3)

# Test to delete user
driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'example')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.close()
