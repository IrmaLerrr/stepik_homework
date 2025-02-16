from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import Select
import time
import math
# import os
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def pass_robot_capch():
  x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
  assert x is not None, "x is not found"
  y = calc(x)
  
  input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
  input1.send_keys(y)
  
  button = browser.find_element(By.CSS_SELECTOR, "#solve")
  button.click()
  
  alert = browser.switch_to.alert
  alert_text = alert.text
  alert_text = alert_text.split(': ')[1]
  pyperclip.copy(alert_text)
  print(pyperclip.paste())

try: 
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser.get(link)
  
  price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
  
  button = browser.find_element(By.CSS_SELECTOR, "#book")
  button.click()  
  
  pass_robot_capch()
  
finally:
  time.sleep(10)
  browser.quit()
