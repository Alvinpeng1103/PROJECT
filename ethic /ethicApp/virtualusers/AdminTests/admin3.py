from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(30)


# Test to add Application
driver.get("http://localhost:8000/admin/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("admin")
time.sleep(3)
driver.find_element_by_name("password").send_keys("admin")
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Applications')]").click()
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Add application')]").click()
time.sleep(3)
select = Select(driver.find_element_by_name("user"))
time.sleep(3)
select.select_by_value("1")
time.sleep(3)
driver.find_element_by_name("title").send_keys("a")
time.sleep(3)
driver.find_element_by_name("supervisor").send_keys("b")
time.sleep(3)
driver.find_element_by_name("status").send_keys("c")
time.sleep(3)
driver.find_element_by_name("_save").click()
time.sleep(3)


# Test to modify application
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Application object (103)')]").click()
driver.find_element_by_name("status").send_keys(" another hello")
time.sleep(3)
driver.find_element_by_name("_continue").click()
time.sleep(3)


# Test to delete application
driver.find_element_by_xpath("//*[contains(text(), 'Applications')]").click()
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Application object (103)')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.close()
