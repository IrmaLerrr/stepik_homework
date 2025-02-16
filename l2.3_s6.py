from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import Select
import time
import math
import os
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser.get(link)
  
  button = browser.find_element(By.TAG_NAME, "button")
  button.click()
  
  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)
    
  x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
  assert x is not None, "x is not found"
  y = calc(x)
  
  input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
  input1.send_keys(y)
  
  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("arguments[0].scrollIntoView(true);", button)
  button.click()
  
  alert = browser.switch_to.alert
  alert_text = alert.text
  alert_text = alert_text.split(': ')[1]
  pyperclip.copy(alert_text)
  print(pyperclip.paste())
  
finally:
  time.sleep(10)
  browser.quit()
