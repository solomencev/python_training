
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

def test_available_currencies():
    currencies = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/button/span').click()
    count = (len(driver.find_elements_by_class_name('select-list__item')))
    assert count >= 16

def test_names_services():
    driver.find_element_by_class_name('navbar-services__icon').click()
    map_of_prices = driver.find_element_by_xpath('//*[@title="Карта низких цен"]').text
    assert map_of_prices == 'Карта низких цен'

    calendar_of_prices = driver.find_element_by_xpath('//*[@title="Календарь низких цен"]').text
    assert calendar_of_prices == 'Календарь низких цен'

    bot = driver.find_element_by_xpath('//*[@title="Бот низких цен"]').text
    assert bot == 'Бот низких цен'

    articles_of_travel = driver.find_element_by_xpath('//*[@title="Статьи о путешествиях"]').text
    assert articles_of_travel == 'Статьи о путешествиях'

    specials = driver.find_element_by_xpath('//*[@title="Спецпредложения"]').text
    assert specials == 'Спецпредложения'

    business = driver.find_element_by_xpath('//*[@title="Для бизнеса"]').text
    assert business == 'Для бизнеса\nB2B'