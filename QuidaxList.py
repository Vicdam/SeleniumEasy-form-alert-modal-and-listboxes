import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://demo.seleniumeasy.com/')
driver.implicitly_wait(20)

# Navigate to List
driver.find_element(By.ID, "at-cv-lightbox-close").click()
driver.find_element(By.XPATH, "//div[@id='navbar-brand-centered']/ul[2]/li[3]/a[1]").click()
driver.find_element(By.XPATH, "//a[@href='./bootstrap-dual-list-box-demo.html']").click()

# Select all list items
driver.find_element(By.XPATH, "//a[contains(@class,'btn btn-default')]").click()
driver.find_element(By.XPATH, "(//a[contains(@class,'btn btn-default')])[2]").click()

# Move all items in the list left and then right
driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-default')]").click()
driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-default')])[2]").click()

# Deselect all items in the two lists
driver.find_element(By.XPATH, "//a[contains(@class,'btn btn-default')]").click()
driver.find_element(By.XPATH, "(//a[contains(@class,'btn btn-default')])[2]").click()

# Select and move 2 items in the list to the left
driver.find_element(By.XPATH, "//li[@class='list-group-item']").click()
driver.find_element(By.XPATH, "(//li[@class='list-group-item'])[2]").click()
driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-default')]").click()

# Test lists search box
driver.find_element(By.XPATH, "//input[@name='SearchDualList']").send_keys("bootstrap-duallist")

# close active browser
driver.quit()
