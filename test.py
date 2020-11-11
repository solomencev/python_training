import time
from selenium.webdriver.chrome.webdriver import WebDriver


def test():
    driver = WebDriver(executable_path=r'C://Python39/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.aviasales.ru/')
    time.sleep(2)
    driver = driver.find_element_by_class_name('_button_text_3oKFG').text
    assert driver == 'Найти билеты'
    print(None)
    ...