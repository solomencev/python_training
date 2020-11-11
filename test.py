import time
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver(executable_path=r'C://Python39/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.aviasales.ru/')


def test_name_of_submit():
    submit = driver.find_element_by_class_name('_button_text_3oKFG').text
    assert submit == 'Найти билеты'

def test_switching_theme():
    switch = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/label/span/span').click()
    assert switch == None
    switch = driver.find_element_by_class_name('_theme_switch_checkbox_30psx').click()
    assert switch == None


    print(None)
    ...