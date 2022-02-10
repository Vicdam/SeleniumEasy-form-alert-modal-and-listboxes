import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

os.environ['PATH'] += r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://demo.seleniumeasy.com/')
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 20)

# Close default Popup
driver.find_element(By.XPATH, "//div[@id='navbar-brand-centered']/ul[2]/li[2]/a[1]").click()

# Navigate to alert and modal
driver.find_element(By.XPATH, "//a[@href='./bootstrap-alert-messages-demo.html']").click()
time.sleep(2)

# Auto close alert 1
driver.find_element(By.ID, "autoclosable-btn-success").click()


def demo_gettext():
    text = driver.find_element(By.XPATH, "//div[@class='col-md-6']//div[1]").text
    print("This is alert 1 = ", text)
    time.sleep(2)


class DemoGetText:
    pass


findbyid = DemoGetText()
demo_gettext()

# Manual close alert 2
driver.find_element(By.ID, "normal-btn-success").click()


def demo_gettexttwo():
    text2 = driver.find_element(By.XPATH, "(//div[contains(@class,'alert alert-success')])[2]").text
    print("This is alert 2 = ", text2)
    time.sleep(2)


class DemoGetTextTwo:
    pass


demo_gettexttwo()

# Close alert 2
driver.find_element(By.XPATH, "//button[@class='close']").click()

# //////////////// Modal  ///////////////////////
# Single Window Pop up

# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1

# Navigate to Popup and modal
driver.find_element(By.XPATH, "//div[@id='navbar-brand-centered']/ul[2]/li[2]/a[1]").click()
driver.find_element(By.XPATH, "//a[@href='./window-popup-modal-demo.html']").click()

driver.find_element(By.LINK_TEXT, "Follow On Twitter").click()

# Wait for the twitter window
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Wait for the twitter window to finish loading content
wait.until(EC.title_contains("Twitter"))

# Test that twitter window is being controlled and close it
driver.find_element(By.NAME, "session[username_or_email]").send_keys("Victor")
driver.close()

# Multiple window popup
driver.switch_to.window(original_window)
driver.find_element(By.XPATH, "//a[@class='btn btn-primary ']").click()

wait.until(EC.number_of_windows_to_be(3))
# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        wait.until(EC.title_contains("Facebook"))
        driver.close()
        break
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        wait.until(EC.title_contains("Twitter"))
        driver.close()
        break

# close active browser
driver.quit()
