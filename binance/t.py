import requests


proxies = {"http":"http://kachanovandrii:Zpxd4tZZVc@149.126.237.25:50100",
           "https":"https://kachanovandrii:Zpxd4tZZVc@149.126.237.25:50100"}

r = requests.get('http://2ip.ru/', proxies=proxies)
url = 'https://2ip.ru/'
print(2)
print(r.text)