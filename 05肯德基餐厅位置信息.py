import requests
import json

url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers={

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',

}
adress=input('输入地址：')
data={
'cname': '',
'pid': '',
'keyword': adress,
'pageIndex': '1',
'pageSize': '10',
}
adressInfo=requests.post(url=url,data=data,headers=headers).text

fp=open('./肯德基位置.txt','w',encoding='utf-8')
fp.write(adressInfo)
print('over')
