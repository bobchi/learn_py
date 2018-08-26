from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.PhantomJS()

driver.get('https://www.baidu.com')
search_kw = driver.find_element_by_id('kw')
search_kw.send_keys('陆良论坛')  # 填充文本

search_btn = driver.find_element_by_id('su')
search_btn.click()  # 点击按钮

WebDriverWait(driver, 10).until(expected_conditions.title_contains('陆良论坛'))

print(driver.page_source)

