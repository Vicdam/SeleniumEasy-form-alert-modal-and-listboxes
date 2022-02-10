import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://demo.seleniumeasy.com/')
driver.implicitly_wait(20)

# Navigate to Input Forms
driver.find_element(By.ID, "at-cv-lightbox-close").click()
driver.find_element(By.LINK_TEXT, "Input Forms").click()
driver.find_element(By.XPATH, "//a[@href='./basic-first-form-demo.html']").click()

# Single Input Field
driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys('Quidax')
driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()


def demo_gettext():
    text = driver.find_element(By.ID, "display").text
    print(text)
    time.sleep(2)


class DemoGetText:
    pass


findbyid = DemoGetText()
demo_gettext()

# Sum form

driver.find_element(By.ID, "sum1").send_keys(4)
driver.find_element(By.ID, "sum2").send_keys(2)

driver.find_element(By.XPATH, "(//button[@class='btn btn-default'])[2]").click()


def demo_gettexttwo():
    text = driver.find_element(By.ID, "displayvalue").text
    print(text)
    time.sleep(2)


class DemoGetTexttwo:
    pass


demo_gettexttwo()

# close active browser
driver.quit()
