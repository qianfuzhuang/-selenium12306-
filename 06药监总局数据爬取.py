import json

import requests

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}
id_list=[]
# id获取
url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
for page in range(1,6):
    page=str(page)
    data={
    'on': 'true',
    'page': page,
    'pageSize': '15',
    'productName':'' ,
    'conditionType': '1',
    'applyname': '',
    'applysn': '',
    }
    respone=requests.post(url,data,headers).json()
    for id in respone["list"]:
        id_list.append(id['ID'])

# 获取详情页
url1='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
fp=open('./化妆公司.json','w',encoding='utf-8')
for id in id_list:
    data_id={
        'id': id
    }
    respone=requests.post(url1,data_id,headers).json()

    json.dump(respone,fp,ensure_ascii=False)
print('结束')
