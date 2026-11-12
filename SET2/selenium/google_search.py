from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Docker")
    search_box.submit()
    input("Search completed. Press Enter to close the browser...")
finally:
    driver.quit()
