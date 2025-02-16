from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    img1 = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = img1.get_attribute("valuex")
    assert x is not None, "valuex is not found"
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
  
    alert = Alert(browser)
    alert_text = alert.text
    print("Текст в alert:", alert_text)
    
finally:
    time.sleep(10)
    browser.quit()
