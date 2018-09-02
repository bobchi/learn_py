# 基金抓取

from urllib import request
import chardet  # 自动检测编码的包
from bs4 import BeautifulSoup
# 爬虫相关
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing.managers import BaseManager
from multiprocessing import Process
import os
# 导入数据库相关
from sqlalchemy import create_engine, desc, text
from common.config import db_url
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from mappers.Myfund import Myfund as my_fund


page1_url = 'http://fund.eastmoney.com/fund.html'
page2_url = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=2,200&dt=1534979287462&atfc=&onlySale=0'


def get_html(page_url):
    response = request.urlopen(page_url)
    raw_html = response.read()
    get_encoding = chardet.detect(raw_html)['encoding']  # 检测网页编码
    return raw_html.decode(get_encoding, 'ignore')


def get_page_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    page_count = soup.find('div', id='pager').find('span', 'nv').get_text()
    return (''.join(filter(str.isdigit, page_count)))   # 提取字符串中的数字


bm = BaseManager(address=('', 8084), authkey=b'12345')
driver = None
all_page = 0


# 初始化并获取页面总数
def init_spider():
    driver = webdriver.PhantomJS()
    driver.get(page1_url)
    page_str = driver.find_element_by_id('pager').find_element_by_xpath('span[@class="nv"]').text
    all_page = int(''.join(filter(str.isdigit, page_str)))


# 将页面数据存入本地txt文件
def get_html_raw(my_range):
    for x in my_range:
        tonum = driver.find_element_by_id('tonum')
        btn_jump = driver.find_element_by_id('btn_jump')
        tonum.clear()
        tonum.send_keys(str(x))
        btn_jump.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('pager')\
            .find_element_by_xpath('span[@value={0} and @class!="end page"]'.format(x))\
            .get_attribute('class').find('at') != -1)
        with open('./htmls/pages_{0}.txt'.format(x), 'wb') as f:
            f.write(driver.find_element_by_id('tableDiv').get_attribute('innerHTML').encode('utf-8'))
            f.close()


# 爬虫多进程运行函数
def begin_spider():
    if(driver == None):
        print('请先运行init_spider初始化')
        exit()
    r = range(1, int(all_page + 1))
    step = 10
    range_list = [r[x:x+step] for x in range(0, len(r), step)]
    process_list = []
    for r in range_list:
        p = Process(target=get_html_raw, args=(r,))
        process_list.append(p)
        p.start()
    for p in process_list:
        p.join()


# 处理净值字符串中的异常
def get_txt(element):
    if element != None:
        txt = element.get_text()
        if str(txt).strip() == '---':
            txt = '0'
        return txt


# 从保存下来的txt中提取数据
def get_fund_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    fund_table = soup.find('table', id='oTable')
    fund_codes = fund_table.tbody.find_all('td', 'bzdm')    # 基金编码集合
    fund_date = fund_table.thead.find('td', colspan='2').get_text()    # 获取基金时间
    result = []
    for fund_code in fund_codes:
        result.append({'fcode': fund_code.get_text(),
                       'fname': fund_code.next_sibling.find('a').get_text(),
                       'NAV': get_txt(fund_code.next_sibling.next_sibling),
                       'ACCNAV': get_txt(fund_code.next_sibling.next_sibling.next_sibling),
                       'DGV': fund_code.parent.find('td', 'rzzz').get_text(),  # 日增长值
                       'DGR': fund_code.parent.find('td', 'rzzl').get_text(),  # 日增长率
                       'fee': get_txt(fund_code.parent.find('div', 'rate_f')),
                       'updatetime': datetime.now().isoformat(sep=' ', timespec='seconds'),
                       'fdate': fund_date
                       })
    return result


# 保存到数据库
engine = create_engine(db_url, echo=True)

def save_db():
    data_dir = '../htmls'
    dir_list = os.listdir(data_dir)
    my_session = sessionmaker(engine)()
    data_list = []
    for p in dir_list:
        if os.path.isfile(os.path.join(data_dir, p)):
            with open(os.path.join(data_dir, p), 'rb') as f:
                html_raw = f.read().decode('utf-8')
                f.close()
            fund_data = get_fund_data(html_raw)
            for result in fund_data:
                fund = my_fund(**result)
                my_session.merge(fund)
                data_list.append(fund)
    my_session.commit()
    my_session.close()


if __name__ == '__main__':
    save_db()

