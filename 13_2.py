from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()

driver.get('http://fund.eastmoney.com/fund.html')

page_text = driver.find_element_by_id('pager').find_element_by_xpath('span[@class="nv"]').text

page_count = ''.join(filter(str.isdigit, page_text))

# 得到第2页数据
page_btn = driver.find_element_by_id('pager').find_element_by_xpath('span[@value="2"]')
page_btn.click()
def is_at(driver):
    return driver.find_element_by_id('pager').find_element_by_xpath('span[@value="2"]')\
        .get_attribute('class').find('at') != -1

WebDriverWait(driver, 10).until(is_at)

print(driver.page_source)


