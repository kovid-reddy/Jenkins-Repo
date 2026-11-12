from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("https://www.wikipedia.org")
    driver.save_screenshot("wikipedia.png")
    print("Screenshot saved as wikipedia.png")
finally:
    driver.quit()
