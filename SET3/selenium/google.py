from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("https://www.google.com")
    input("Google opened. Press Enter to close the browser...")
finally:
    driver.quit()
