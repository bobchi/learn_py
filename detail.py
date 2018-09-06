# fund detail
from urllib import request
import chardet  # 自动检测编码的包
# 爬虫相关
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from threading import Thread, Lock

# 导入数据库相关
import os
from sqlalchemy import create_engine, desc, text
from common.config import db_url
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from mappers.Myfund import Myfund as my_fund


#   初始化爬虫
def spider_init():
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', firefox_options=options)
    driver.get('http://fundf10.eastmoney.com/jjjz_004616.html')
    page_count = driver.find_element_by_id('pagebar')\
        .find_element_by_xpath('div[@class="pagebtns"]/label[text()="下一页"]/preceding-sibling::label[1]').text
    with open('./detail/count.txt', 'wb') as f:
        f.write(page_count.encode('utf-8'))
        f.close()
    page_count = int(page_count)
    return driver, page_count


#   将网页源码存入本地文件夹
def get_html_raw(detail_range, driver, lock):
    for x in detail_range:
        lock.acquire()
        if x == 1:
            pass
        else:
            pnum = driver.find_element_by_id('pagebar').find_element_by_xpath('div[@class="pagebtns"]/input[@class="pnum"]')
            pgo = driver.find_element_by_id('pagebar').find_element_by_xpath('div[@class="pagebtns"]/input[@class="pgo"]')
            pnum.clear()
            pnum.send_keys(str(x))
            pgo.click()
            # WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('pagebar').find_element_by_xpath('label[@value="{0}" and @class="cur"]'.format(x)) != None)
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("pagebar").find_element_by_xpath(
                "div[@class='pagebtns']/label[@value={0} and @class='cur']".format(x)) != None)
        with open('./detail/d_{0}.txt'.format(x), 'wb') as f:
            f.write(driver.find_element_by_id('jztable').get_attribute('innerHTML').encode('utf-8'))
            f.close()
            lock.release()


#   开始多进程抓取
def begin_spider():
    (driver, page_count) = spider_init()
    r = range(1, page_count+1)
    lock = Lock()
    step = 5
    range_list = [r[x:x + step] for x in range(0, len(r), step)]
    thread_list = []
    for ran in range_list:
        t = Thread(target=get_html_raw, args=(ran, driver, lock))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()
    print('抓取完成')


if __name__ == '__main__':
    # spider_init()
    # print(driver)
    begin_spider()
