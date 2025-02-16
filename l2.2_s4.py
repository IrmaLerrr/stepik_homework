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
  browser.execute_script("document.title='Script executing';alert('Robots at work');")
    
finally:
  time.sleep(10)
  browser.quit()
