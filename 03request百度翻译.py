import json

import requests

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'

}
post_url='https://fanyi.baidu.com/sug'
word=input('输入一个单词:')
data={
     'kw':word
}
respone=requests.post(url=post_url,data=data,headers=headers)
text=respone.json()
fileName=word+'.json'
fp=open(fileName,'w',encoding='utf-8')
json.dump(text,fp=fp,ensure_ascii=False)
print('over')
