from selenium_utils import webdriver, By, time

link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(30)
    browser.quit()

