from pymongo import MongoClient
import requests
from fake_useragent import UserAgent
import time


client = MongoClient()
db = client.lagou
lagou = db.pachong
def get_job_info(page, keyword):
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    headers = {
            'Cookie': 'JSESSIONID=ABAAABAABEEAAJA056CAD85932E542C97E3C75AC57647E4; _ga=GA1.2.302262330.1521882979; _gid=GA1.2.2071000378.1521882979; index_location_city=%E6%B7%B1%E5%9C%B3; user_trace_token=20180324171739-00a5a016-8463-4097-a1b7-835ab1dcdc77; LGSID=20180324171824-4ddbb0d9-2f44-11e8-b606-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; LGUID=20180324171824-4ddbb39e-2f44-11e8-b606-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521883105; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521883519; LGRID=20180324172522-4700c949-2f45-11e8-9b5d-525400f775ce; SEARCH_ID=1473baba22fb4fedbd4b4fdec0fd70bc',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=',
            }

    for i in range(1, page+1):
        payload = { 'first': 'false',
                    'pn': i,
                    'kd': keyword,
        }
        useragent = UserAgent()
        headers['User-Agent'] = useragent.random
        response = requests.post(url, data = payload, headers = headers)
        print('正在爬取第' + str(i) + '页的数据')

        if response.status_code == 200:
            job_json = response.json()['content']['positionResult']['result']
            lagou.insert(job_json)
        else:
            print('Something Wrong!')

        time.sleep(3)

if __name__ == '__main__':
    get_job_info(3, '爬虫')