import requests

# 根据协议类型，选择不同的代理
proxies={'http':'socks5://127.0.0.1:1080','https':'socks5://127.0.0.1:1080'}

url='https://www.baidu.com'
response=requests.get(url,proxies=proxies,timeout=10)
print(response.status_code)