# Краткое описание `expected_conditions` в Selenium

## 1. **`title_is(title)`**
- **Описание**: Ожидает, что заголовок страницы точно совпадает с `title`.
- **Пример**:
  ` wait.until(EC.title_is("Google")) `

## 2. **`title_contains(text)`**
- **Описание**: Ожидает, что заголовок страницы содержит `text`.
- **Пример**:
  ` wait.until(EC.title_contains("Search")) `

## 3. **`presence_of_element_located(locator)`**
- **Описание**: Ожидает, что элемент появится в DOM (не обязательно видимый).
- **Пример**:
  ` wait.until(EC.presence_of_element_located((By.ID, "my-element"))) `

## 4. **`visibility_of_element_located(locator)`**
- **Описание**: Ожидает, что элемент появится в DOM **и** будет видимым.
- **Пример**:
  ` wait.until(EC.visibility_of_element_located((By.ID, "my-element"))) `

## 5. **`visibility_of(element)`**
- **Описание**: Ожидает, что конкретный элемент (уже найденный) станет видимым.
- **Пример**:
  ` wait.until(EC.visibility_of(element)) `

## 6. **`presence_of_all_elements_located(locator)`**
- **Описание**: Ожидает, что **все элементы**, соответствующие локатору, появятся в DOM.
- **Пример**:
  ` wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item"))) `

## 7. **`text_to_be_present_in_element(locator, text)`**
- **Описание**: Ожидает, что текст `text` появится внутри элемента.
- **Пример**:
  ` wait.until(EC.text_to_be_present_in_element((By.ID, "status"), "Success")) `

## 8. **`text_to_be_present_in_element_value(locator, text)`**
- **Описание**: Ожидает, что текст `text` появится в значении атрибута `value` элемента.
- **Пример**:
  ` wait.until(EC.text_to_be_present_in_element_value((By.ID, "input"), "John")) `

## 9. **`frame_to_be_available_and_switch_to_it(locator)`**
- **Описание**: Ожидает, что фрейм станет доступным и переключается на него.
- **Пример**:
  ` wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-frame"))) `

## 10. **`invisibility_of_element_located(locator)`**
- **Описание**: Ожидает, что элемент станет невидимым или исчезнет из DOM.
- **Пример**:
  ` wait.until(EC.invisibility_of_element_located((By.ID, "loader"))) `

## 11. **`element_to_be_clickable(locator)`**
- **Описание**: Ожидает, что элемент станет кликабельным (видимым и enabled).
- **Пример**:
  ` wait.until(EC.element_to_be_clickable((By.ID, "submit-button"))) `

## 12. **`staleness_of(element)`**
- **Описание**: Ожидает, что элемент больше не привязан к DOM (удален или обновлен).
- **Пример**:
  ` wait.until(EC.staleness_of(element)) `

## 13. **`element_to_be_selected(element)`**
- **Описание**: Ожидает, что элемент (например, чекбокс) будет выбран.
- **Пример**:
  ` wait.until(EC.element_to_be_selected(element)) `

## 14. **`element_located_to_be_selected(locator)`**
- **Описание**: Ожидает, что элемент, найденный по локатору, будет выбран.
- **Пример**:
  ` wait.until(EC.element_located_to_be_selected((By.ID, "checkbox"))) `

## 15. **`element_selection_state_to_be(element, is_selected)`**
- **Описание**: Ожидает, что элемент будет в определенном состоянии (выбран или не выбран).
- **Пример**:
  ` wait.until(EC.element_selection_state_to_be(element, True)) `

## 16. **`element_located_selection_state_to_be(locator, is_selected)`**
- **Описание**: Ожидает, что элемент, найденный по локатору, будет в определенном состоянии.
- **Пример**:
  ` wait.until(EC.element_located_selection_state_to_be((By.ID, "checkbox"), True)) `

## 17. **`alert_is_present()`**
- **Описание**: Ожидает, что появится alert-окно.
- **Пример**:
  ` alert = wait.until(EC.alert_is_present()) `