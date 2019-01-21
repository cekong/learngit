''''''
'''

获取access_token

'''
import requests



def GetToken(API_KEY,SECRET_KEY):
      url = 'https://aip.baidubce.com/oauth/2.0/token?' \
            'grant_type=client_credentials&' \
            'client_id='+API_KEY+'&' \
            'client_secret='+SECRET_KEY
      response=requests.get(url)
      print('access_token=',response.json()['access_token'])
      return response.json()['access_token']
