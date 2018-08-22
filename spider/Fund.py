# 基金抓取

from bs4 import BeautifulSoup
from urllib import request
import chardet  # 自动检测编码的包
from bs4 import BeautifulSoup

page1_url = 'http://fund.eastmoney.com/fund.html'

def get_html(page_url):
    response = request.urlopen(page_url)
    raw_html = response.read()
    get_encoding = chardet.detect(raw_html)['encoding']  # 检测网页编码
    return raw_html.decode(get_encoding)

def get_page_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    page_count = soup.find('div', id='pager').find('span', 'nv').get_text()
    return (''.join(filter(str.isdigit, page_count)))   # 提取字符串中的数字


