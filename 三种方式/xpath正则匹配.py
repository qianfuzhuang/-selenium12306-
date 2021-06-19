import requests
from lxml import etree
import os

url='https://pic.netbian.com/4kdongman/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',

}
if not os.path.exists('./彼岸图'):
    os.mkdir('./彼岸图')

respone=requests.get(url,headers).text
tree=etree.HTML(respone)
img_li=tree.xpath('//*[@id="main"]/div[3]/ul/li')
for img in img_li:
    img_url='https://pic.netbian.com/'+img.xpath('./a/img/@src')[0]
    img_data=requests.get(img_url,headers).content
    img_name=img_url.split('/')[-1]
    imgpath='./彼岸图/'+img_name
    with open(imgpath,'wb')as fp:
        fp.write(img_data)
    print(img_name,'成功')



# 若出现乱码有2种方式
# 1.respone.encoding='utf-8'
# 2.name.encode('iso-8859-1').decode('utf-8' )
