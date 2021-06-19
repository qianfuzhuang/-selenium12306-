import requests
import json

url='https://movie.douban.com/j/chart/top_list?'
headers={

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',

}
param={
'type':'11',
'interval_id': '100:90',
'action':' ',
'start':'0',
'limit':'100',
}
respone=requests.get(url=url,params=param,headers=headers)
list_data=respone.json()
fp=open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print('over')
