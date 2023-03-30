import threading
import time

import requests
import json

#a = requests.post('https://www.binance.com/bapi/futures/v1/public/future/leaderboard/getOtherPosition', data={'encryptedUid':'8D27A8FA0C0A726CF01A7D11E0095577', 'tradeType':'PERPETUAL'})

url = r'https://www.binance.com/bapi/futures/v1/public/future/leaderboard/getOtherPerformance'

headers = {'content-type': 'application/json'}
arg = '24B04BB890EE750DBA4BD16009365235'

json_data = {
    "encryptedUid": f'{arg}',
    "tradeType": 'PERPETUAL'
}

#
response = requests.post(url, headers=headers, json=json_data)
if response.status_code != 200:
    response.raise_for_status()
print(response.text)
data = json.loads(response.text)['data']
print(data)
pnl = 0
for i in data:
    if i['periodType'] == 'DAILY' and i['statisticsType'] == 'ROI':
        if round(float(abs(i['value'])), 1) == 0.0:
            roi = 0
        else:
            roi = float(i['value'])
    if i['periodType'] == 'DAILY' and i['statisticsType'] == 'PNL':
        if round(float(abs(i['value'])), 1) == 0.0:
            print(1)
            pnl = 0
        else:
            print(2)
            pnl = float(i['value'])
            print(pnl)
    if roi == 0 and i['periodType'] == 'WEEKLY' and i['statisticsType'] == 'ROI':
        roi = float(i['value'])
    if pnl == 0 and i['periodType'] == 'WEEKLY' and i['statisticsType'] == 'PNL':
        pnl = float(i['value'])
print(f'ROI - {roi}. PNL - {pnl}')
if pnl > 0:
    dep = abs(pnl) * 100 / (100 * abs(roi)) + abs(pnl)
    print(dep)
if pnl < 0:
    dep = abs(pnl) * 100 / (100 * abs(roi)) - abs(pnl)
    print(dep)
#except Exception as e:
#    print(e)