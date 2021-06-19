import requests

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
if __name__=="__main__":
    url='https://www.sogou.com/web'
    kw=input('enter a word:')

    param={
        'query':kw
    }
    respone=requests.get(url=url,params=param,headers=headers)
    page_text=respone.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')