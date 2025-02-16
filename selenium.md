# Как установить виртуальное окружение
```bash
mkdir environments
cd environments
python -m venv selenium_env
environments\selenium_env\Scripts\activate.bat
environments\selenium_env\Scripts\deactivate.bat
```

# Поиск элементов
`find_element(By.ID, value)` — поиск по уникальному атрибуту id элемента.
`find_element(By.CSS_SELECTOR, value)` — поиск элемента с помощью правил на основе CSS.
`find_element(By.XPATH, value)` — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
`find_element(By.NAME, value)` — поиск по атрибуту name элемента;
`find_element(By.TAG_NAME, value)` — поиск элемента по названию тега элемента;
`find_element(By.CLASS_NAME, value)` — поиск по значению атрибута class;
`find_element(By.LINK_TEXT, value)` — поиск ссылки на странице по полному совпадению;
`find_element(By.PARTIAL_LINK_TEXT, value)` — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

# XPath
Символ / аналогичен символу > в CSS-селекторе, а символ // — пробелу. Их смысл:
`el1/el2` — выбирает элементы el2, являющиеся прямыми потомками el1;
`el1//el2` — выбирает элементы el2, являющиеся потомками el1 любой степени вложенности.
Kогда мы начинаем запрос с символа /,  мы должны указать элемент, являющийся корнем нашего документа. Корнем всегда будет элемент с тегом <html>. 
`/html/body/header`
Мы можем начинать запрос и с символа //. Это будет означать, что мы хотим найти всех потомков корневого элемента без указания корневого элемента. 
`//header`

### Фильтрация 
Символ [ ] — это команда фильтрации. Если по запросу найдено несколько элементов, то будет произведена фильтрация по правилу, указанному в скобках.
`//img[@id='bullet']` - фильтрация по id
`//div[@class="row"]/div[2]` фильтрация по номеру
`//p[text()="Lenin cat"]` - поиск по тексту внутри
`//p[contains(text(), "cat")]` - поиск по части текста
`//div[contains(@class, "navbar")]` - поиск по частичному совпадению атрибутов, напрмер поиск по классу, если их несколько у одного элемента
`//img[@name='bullet-cat' and @data-type='animal']` - можно использовать булевы операции (and, or, not)

### Символ * — команда выбора всех элементов
`//div/*[@class="jumbotron-heading"]` - обычно Xpath взвращает один элемент?

### Поиск по классу в XPath регистрозависим

### Полезные ссылки
https://www.w3schools.com/xml/xpath_syntax.asp

https://msdn.microsoft.com/ru-ru/library/ms256086(v=vs.120).aspx

https://msiter.ru/tutorials/xpath/syntax

https://habr.com/post/114772/

https://testerslittlehelper.wordpress.com/2016/07/10/real-xpath/

https://devhints.io/xpath

# Работа с чекбоксами
```python
option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()
```
если есть label
```python
option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
option1.click()
```
# Работа со списками
```python
browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# или
# browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
```
```python
from selenium.webdriver.support.ui import Select

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с value 1
select.select_by_visible_text("text") # ищем элемент с текстом "text"
select.select_by_index(1) # ищем элемент по порядковому номеру, 0 - это выбранный по умолчанию

```
# Как вставлять код java script
`browser.execute_script("document.title='Script executing';alert('Robots at work');")`

# Как работать с алертами
```python
alert = browser.switch_to.alert
alert.accept()

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
```

# Как переключаться между страницами
```python
browser.switch_to.window(new_window)
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
```
# Как настроить ожидание
команда искать каждый элемент в течение 5 секунд
`browser.implicitly_wait(5)`
команда для одной кнопки проверять ее в течение 5 секунд, пока кнопка не станет кликабельной
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
..
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
```
### Остальные правила в expected_conditions:

-title_is
-title_contains
-presence_of_element_located
-visibility_of_element_located
-visibility_of
-presence_of_all_elements_located
-text_to_be_present_in_element
-text_to_be_present_in_element_value
-frame_to_be_available_and_switch_to_it
-invisibility_of_element_located
-element_to_be_clickable
-staleness_of
-element_to_be_selected
-element_located_to_be_selected
-element_selection_state_to_be
-element_located_selection_state_to_be
-alert_is_present

Описание каждого правила можно найти здесь https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# Полезные ссылки

http://chromedriver.chromium.org/getting-started
https://www.guru99.com/selenium-tutorial.html — Туториал на английском, ориентирован на Java.
https://www.guru99.com/live-selenium-project.html — Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.
http://barancev.github.io/good-locators/ — что такое хорошие селекторы
http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная? 
https://www.selenium.dev/documentation/webdriver/waits/
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
https://blog.codeship.com/get-selenium-to-wait-for-page-load/
http://barancev.github.io/slow-loading-pages/
http://barancev.github.io/page-loading-complete/