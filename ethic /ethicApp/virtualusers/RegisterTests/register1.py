from selenium import webdriver
import time
import os

# Test to see if go back hyperlink works

# Get chrome driver
dir_path = os.path.dirname(os.path.realpath(__file__))
driver = webdriver.Chrome(dir_path + "/chromedriver")
driver.set_page_load_timeout(10)

# Run the website on local machine in localhost, port 8000.
driver.get("http://localhost:8000/register/")
time.sleep(3)
driver.find_element_by_xpath("//*[contains(text(), 'Go back')]").click()
time.sleep(3)
driver.close()
