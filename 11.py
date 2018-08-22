from spider.Fund import get_html, page1_url, get_page_count
import execjs

# ret = get_html(page1_url)
#
# print(get_page_count(ret))

js_engine = execjs.get()
print(js_engine.eval("1+33"))
# print(ret)


