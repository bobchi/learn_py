from spider.Fund import get_html, page1_url, get_page_count
import execjs
from spider.Fund import page1_url, get_html, page2_url
import demjson
# ret = get_html(page1_url)
# print(get_page_count(ret))

# js_engine = execjs.get()
# print(js_engine.eval("1+33"))
html_raw = get_html(page2_url)
json_str = html_raw[7:]
json_str = demjson.decode(json_str)
print(json_str['datas'])

# cpl = js_engine.compile(js)

# print(cpl.call('get_db'))


