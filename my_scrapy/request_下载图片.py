import requests




def download_image():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    url="https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/w=268/sign=6053fac19c510fb378197091e132c893/728da9773912b31b36cf79518418367adab4e123.jpg"
    response=requests.get(url,headers=headers)
    with open('test.jpg', 'wb') as f:
        f.write(response.content)

download_image()