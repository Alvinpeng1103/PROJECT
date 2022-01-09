from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(30)


# Test to add coversheet questions
driver.get("http://localhost:8000/admin/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("admin")
time.sleep(3)
driver.find_element_by_name("password").send_keys("admin")
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Cover sheet questions')]").click()
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Add cover sheet question')]").click()
time.sleep(3)
driver.find_element_by_name("question_num").send_keys("100000")
time.sleep(3)
driver.find_element_by_name("text").send_keys("a")
time.sleep(3)
driver.find_element_by_name("is_short_answer").send_keys("0")
time.sleep(3)
driver.find_element_by_name("_save").click()
time.sleep(3)


# Test to modify coversheet questions
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'CoverSheetQuestion object (100000)')]").click()
driver.find_element_by_name("text").send_keys(" another hello")
time.sleep(3)
driver.find_element_by_name("_continue").click()
time.sleep(3)


# Test to delete coversheet questions
driver.find_element_by_xpath(
    "//*[contains(text(), 'Cover sheet question')]").click()
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'CoverSheetQuestion object (100000)')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.close()
