from spider.Fund import get_html, page1_url, get_page_count

ret = get_html(page1_url)

print(get_page_count(ret))

