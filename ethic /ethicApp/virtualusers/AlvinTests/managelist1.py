from selenium import webdriver
import time
import os
from selenium.webdriver.support.select import Select


dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/login/")
time.sleep(5)
driver.find_element_by_name("username").send_keys("normal")
time.sleep(5)
driver.find_element_by_name("password").send_keys("POL123@4")
time.sleep(5)
driver.find_element_by_name("Login").click()
time.sleep(5)

driver.find_element_by_xpath("//*[@id='contents']/div[2]/a/button").click()

time.sleep(1)

driver.find_element_by_name("next").click()

select_class = driver.find_element_by_xpath("//*[@id='contents']/div/div/form/div[1]")

elements = Select(select_class)

elements.select_by_value("No")

time.sleep(5)




time.sleep(1)











