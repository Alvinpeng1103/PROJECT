from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(30)


# Test to add Answer
driver.get("http://localhost:8000/admin/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("admin")
time.sleep(3)
driver.find_element_by_name("password").send_keys("admin")
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Answers')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Add answers')]").click()
time.sleep(3)
driver.find_element_by_name("id").send_keys("100000")
time.sleep(3)
driver.find_element_by_name("short_answer_text").send_keys("hello")
time.sleep(3)
select = Select(driver.find_element_by_name("question_id"))
time.sleep(3)
select.select_by_value("101")
time.sleep(3)
select = Select(driver.find_element_by_name("application_id"))
time.sleep(3)
select.select_by_value("1")
time.sleep(3)
driver.find_element_by_name("is_short_answer").send_keys("1")
time.sleep(3)
driver.find_element_by_name("section_name").send_keys("F")
time.sleep(3)
driver.find_element_by_name("is_referenced").send_keys("0")
time.sleep(3)
driver.find_element_by_name("is_exemplar").send_keys("0")
time.sleep(3)
driver.find_element_by_name("answer_type").send_keys("example")
time.sleep(3)
driver.find_element_by_name("_save").click()
time.sleep(3)


# Test to modify answer
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Answers object (100000)')]").click()
driver.find_element_by_name("short_answer_text").send_keys(" another hello")
time.sleep(3)
driver.find_element_by_name("_continue").click()
time.sleep(3)


# Test to delete answer
driver.find_element_by_xpath("//*[contains(text(), 'Answerss')]").click()
time.sleep(3)
driver.find_element_by_xpath(
    "//*[contains(text(), 'Answers object (100000)')]").click()
driver.find_element_by_xpath("//*[contains(text(), 'Delete')]").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(3)
driver.close()
