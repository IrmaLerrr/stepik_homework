from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
  link = "https://suninjuly.github.io/selects1.html"
  browser = webdriver.Chrome()
  browser.get(link)
  
  # browser.find_element(By.TAG_NAME, "select").click()
  # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
  # browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
  
  # select = Select(browser.find_element(By.TAG_NAME, "select"))
  # select.select_by_value("1") # ищем элемент с текстом "Python"
  # select.select_by_visible_text("text") - поиск элемента по тексту
  # select.select_by_index(index) - поиск по порядковому номеру(ноль - значение по умолчанию, не выбранное)
  
  num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
  assert num1 is not None, "num1 is not found"
  num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
  assert num2 is not None, "num2 is not found"
  sum = int(num1) + int(num2)
  print(sum)
  
  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_visible_text(str(sum))

  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()

  time.sleep(1)

  alert = Alert(browser)
  alert_text = alert.text
  print("Текст в alert:", alert_text)
    
finally:
  time.sleep(10)
  browser.quit()
