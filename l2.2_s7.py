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
  link = "http://suninjuly.github.io/file_input.html"
  browser.get(link)
  
  input1 = browser.find_element(By.NAME, "firstname")
  assert input1 is not None, "firstname is not found"
  input1.send_keys("firstname")
  
  input2 = browser.find_element(By.NAME, "lastname")
  assert input2 is not None, "lastname is not found"
  input2.send_keys("lastname")
  
  input3 = browser.find_element(By.NAME, "email")
  assert input3 is not None, "email is not found"
  input3.send_keys("email")
  
  input4 = browser.find_element(By.NAME, "file")  
  assert input4 is not None, "file is not found"
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, 'file.txt')
  # print(os.path.abspath(__file__))
  # print(os.path.abspath(os.path.dirname(__file__)))
  input4.send_keys(file_path)
    
  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("arguments[0].scrollIntoView(true);", button)
  button.click()
    
  # alert = browser.switch_to.alert
  # alert_text = alert.text
  # print("Текст в alert:", alert_text)
  
  alert = browser.switch_to.alert
  alert_text = alert.text
  alert_text = alert_text.split(': ')[1]
  pyperclip.copy(alert_text)
  print(pyperclip.paste())
  
finally:
  time.sleep(10)
  browser.quit()
