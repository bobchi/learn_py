from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()

driver.get('http://fund.eastmoney.com/fund.html')

page_text = driver.find_element_by_id('pager').find_element_by_xpath('span[@class="nv"]').text

page_count = ''.join(filter(str.isdigit, page_text))

# 循环获取页面数据

def get_data(start, end):
    for x in range(start, end+1):
        tonum = driver.find_element_by_id('tonum')  # 获取文本框
        btn_jump = driver.find_element_by_id('btn_jump')    # 获取点击按钮
        tonum.clear()
        tonum.send_keys(str(x))
        btn_jump.click()
        WebDriverWait(driver, 20).until(lambda driver:driver.find_element_by_id('pager').find_element_by_xpath('span[@value="{0}" and @class != "end page"]'.format(x))\
                                        .get_attribute("class").find("at") != -1)
        with open('./htmls/page_{0}.txt'.format(x), 'wb') as f:
            f.write(driver.find_element_by_id('tableDiv').get_attribute('innerHTML').encode('utf-8'))
            f.close()


get_data(1, 5)

