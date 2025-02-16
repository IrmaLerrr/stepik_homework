from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  browser = webdriver.Chrome()
  link = "https://SunInJuly.github.io/execute_script.html"
  browser.get(link)
  
  x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
  assert x is not None, "x is not found"
  y = calc(x)
  
  input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
  input1.send_keys(y)
  
  option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
  browser.execute_script("arguments[0].scrollIntoView(true);", option1)
  option1.click()
    
  option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  browser.execute_script("arguments[0].scrollIntoView(true);", option2)
  option2.click()
    
  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("arguments[0].scrollIntoView(true);", button)
  button.click()
    
  alert = Alert(browser)
  alert_text = alert.text
  print("Текст в alert:", alert_text)
  
finally:
  time.sleep(10)
  browser.quit()
