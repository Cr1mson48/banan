import time

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from locale import atof
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('--no-sandbox')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
link = f'https://www.binance.com/ru/futures-activity/leaderboard/user?encryptedUid=4E210DD2B5E59C8F86E44A3717F3CDCD'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# response = requests.get(link, headers=headers)
# soup = BeautifulSoup(response.text, 'lxml')
driver.implicitly_wait(20)
driver.get(link)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')


symb = soup.find_all('div', class_='border-container css-vurnku')

print(symb)
text = ''
for i in symb:
    text = text + i.text

roi = text.split('Ежедневный ROI')
roi = roi[1].split('%PNL')

pnl = text.split('PNL по дням (USD)')
pnl = pnl[1].split('Еженедельный ROI')


if '.' in str(roi):
    roi = roi[0].split('.')
    roi[0] = roi[0].replace(',', '')

if '.' in str(pnl):
    pnl = pnl[0].split('.')
    pnl[0] = pnl[0].replace(',', '')

roi = float(roi[0])
pnl = float(pnl[0])

print(roi)
print(pnl)

dep = pnl * 100 / roi
print(dep)

#print(symb)