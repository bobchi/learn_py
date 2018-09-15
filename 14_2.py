# r = range(1, 32)
# print(r[2:6])
# step = 10
# list = [r[x:x+step] for x in range(0, len(r), step)]

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing import Process, Manager

driver = webdriver.PhantomJS()

driver.get('http://fund.eastmoney.com/fund.html')

page_text = driver.find_element_by_id('pager').find_element_by_xpath('span[@class="nv"]').text

page_count = ''.join(filter(str.isdigit, page_text))


# 循环获取页面数据
def get_data(my_range):
    for x in my_range:
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


r = range(1, int(page_count)+1)
step = 10
range_list = [r[x:x+step] for x in range(0, len(r), step)]
process_list = []

if __name__ == '__main__':
    for x in range_list:
        p = Process(target=get_data, args=(x,))
        process_list.append(p)
    for p in process_list:
        p.start()
