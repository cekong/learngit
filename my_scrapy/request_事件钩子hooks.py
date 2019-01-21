import requests
'''
https://www.imooc.com/video/13091
4-3requests库-事件钩子
'''


'''回调函数'''
def get_key_info(response,*args,**kwargs):
    print(response.headers)


if __name__ == '__main__':
    requests.get('https://www.baidu.com',hooks=dict(response=get_key_info))
