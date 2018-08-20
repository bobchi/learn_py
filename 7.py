from urllib.request import urlopen

response = urlopen('http://fund.eastmoney.com/fund.html')
html = response.read()

with open('./files/2.txt', 'wb') as f:
    f.write(html.decode('gb2312').encode('utf8'))
    f.close()

