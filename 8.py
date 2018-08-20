from bs4 import BeautifulSoup

with open('./files/2.txt', 'rb') as f:
    html = f.read().decode('utf8')
    f.close()

soup = BeautifulSoup(html, 'html.parser')
f_codes = soup.find('table', id='oTable').tbody.find_all('td', 'bzdm')
result = ()
for f_code in f_codes:
    result += ({'code': f_code.get_text()
               , 'name': f_code.next_sibling.find('a').get_text()
               , 'NAV': f_code.next_sibling.next_sibling.get_text()
               , 'ACCNAV': f_code.next_sibling.next_sibling.next_sibling.get_text()},)

print(result)

