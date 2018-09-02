from bs4 import BeautifulSoup

with open('./htmls/page_1.txt', 'rb') as f:
    html = f.read().decode('utf8')
    f.close()

soup = BeautifulSoup(html, 'html.parser')
fund_table = f_codes = soup.find('table', id='oTable')
f_codes = fund_table.tbody.find_all('td', 'bzdm')
fund_date = fund_table.thead.find('td', colspan='2').get_text()
print(fund_date)
result = ()
for f_code in f_codes:
    result += ({'code': f_code.get_text()
               , 'name': f_code.next_sibling.find('a').get_text()
               , 'NAV': f_code.next_sibling.next_sibling.get_text()
               , 'ACCNAV': f_code.next_sibling.next_sibling.next_sibling.get_text()},)

print(result)

