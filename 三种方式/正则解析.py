import os
import re
import requests
for j in range(1,13):
    j+=1
    url='https://www.qiushibaike.com/imgrank/page/%d/'%j
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    }
    if not os.path.exists('./picture'):
        os.mkdir('./picture')
    page_text=requests.get(url,headers).text
    '''<img src="//pic.qiushibaike.com/system/pictures/12443/124438858/medium/2MO91QK51ATU50AN.jpg" alt="糗事#124438858" class="illustration" width="100%" height="auto">'''
    reg='<div class="thumb">.*?<img src="(.*?)"'
    img_list=re.findall(reg,page_text,re.S)
    # print(img_list)
    i=1
    for img in img_list:
        img='https:'+img
        img_info=requests.get(img,headers).content
        imgName=img.split('/')[-1]
        imgpath='./picture/'+imgName
        with open(imgpath,'wb')as fp:
            fp.write(img_info)

print('下载完成')

