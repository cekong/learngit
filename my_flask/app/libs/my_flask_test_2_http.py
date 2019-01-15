''''''
'''
发送http请求两种方式：
1.urllib （models urllib import request)
2.requests （import requests)

'''
import requests

class HTTP:
    @staticmethod
    def get(url,return_json=True):
        r=requests.get(url)
        #restful api返回的结果一般是json格式
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

'''
@staticmethod静态方法
作用：就可以不需要实例化，直接类名.方法名()来调用。
'''
'''
class HTTP:  与 class HTTP(object):
在python3中是一样的
'''