import requests

url='https://pic.qiushibaike.com/system/pictures/12443/124437443/medium/YLJY544J9KLAHI1G.jpg'
# 返回二进制文件
# text字符串   content二进制  json()对象类型响应数据
img_data=requests.get(url).content
with open('./qiutu.jpg','wb')as fp:
    fp.write(img_data)