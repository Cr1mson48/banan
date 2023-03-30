import threading
import time

import requests
import json

#a = requests.post('https://www.binance.com/bapi/futures/v1/public/future/leaderboard/getOtherPosition', data={'encryptedUid':'8D27A8FA0C0A726CF01A7D11E0095577', 'tradeType':'PERPETUAL'})

url = r'https://www.binance.com/bapi/futures/v1/public/future/leaderboard/getOtherPosition'

#a = requests.post(url, data=[('encryptedUid', '8D27A8FA0C0A726CF01A7D11E0095577', ('tradeType', 'PERPETUAL'))])
#print(a.request.body)
#print(a.text)

headers = {'content-type': 'application/json'}

http_proxy = "http://jp.proxiware.com:2000"

proxies = {
    "https": "http://ru.proxiware.com:32000"
}

#8D27A8FA0C0A726CF01A7D11E0095577
def th1(arg, b):
    def open_order(symboul, qty, id, side):
        pass

    def close_order(symboul, id, side):
        pass
    #while True:
    print('поток', b)
    json_data = {
        "encryptedUid": f'{arg}',
        "tradeType": 'PERPETUAL'
    }
    try:
        response = requests.post(url, headers=headers, json=json_data)
        if response.status_code != 200:
            response.raise_for_status()
        data = json.loads(response.text)['data']['otherPositionRetList']
        print(data)
        for i in data:
            print(i)
    except Exception as e:
        print(e)
    time.sleep(2)




#while True:

    #a = input()
    #b = input()
a = 'DB11EA1A52030AD51CC1B43A04AB27C3'
b = 'DB11EA1A52030AD51CC1B43A04AB27C3'
b = threading.Thread(target=th1, args=(a, b))
b.start()
#c = 'A81B9CB3E58B471B269CB88A30EF0190'
#d = 'A81B9CB3E58B471B269CB88A30EF0190'
#b = threading.Thread(target=th1, args=(c, d))
#b.start()



#for i in data:
#    print(i['symbol'])


#url = 'https://2ip.ru/'
#print(1)
#while True:
#    print(2)
#    response = requests.get(url, proxies=proxies)
#
#    print(response.text)