from bs4 import BeautifulSoup
import requests
import lxml

url='https://so.gushiwen.org/guwen/book_46653FD803893E4F7F702BCF1F7CCE17.aspx'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    }
respone=requests.get(url,headers).text
soup=BeautifulSoup(respone,'lxml')
li_list=soup.select('.bookcont>ul>span')
fp=open('./三国演义.txt','w',encoding='utf-8')
for li in li_list:
    title=li.a.string
    detail_url=li.a['href']
    respone1=requests.get(detail_url,headers).text
    soup1=BeautifulSoup(respone1,'lxml')
    detail=soup1.find('div',class_='contson').text
    fp.write(title+'\n'+detail)
    print(title,'爬取成功')
