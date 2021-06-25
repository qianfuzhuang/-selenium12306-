from selenium import webdriver
from time import sleep
from PIL import Image
from selenium.webdriver import ActionChains
from PIL import ImageOps
#!/usr/bin/env python
# coding:utf-8
url='https://kyfw.12306.cn/otn/resources/login.html'
import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

driver=webdriver.Chrome()
driver.get(url)
# 窗口最大化
driver.maximize_window()
sleep(1)
# 切换至账号密码登录
btn=driver.find_element_by_class_name('login-hd-account')
btn.click()

sleep(2)
#用此方法最为简便
# 方法一：
# 直接获取验证码图片
driver.find_element_by_xpath(
    '//*[@id="J-loginImg"]').screenshot('./code.png')
# 找到验证码图片
img_pos=driver.find_element_by_xpath('//*[@id="J-loginImg"]')
# 获取验证码左上角位置

# 方法二
# 截取全屏再截取验证码位置
'''
location=img_pos.location  #x,y
# print(location)
# 获取验证码尺寸
size=img_pos.size
# print(size)
driver.save_screenshot('yzm.png')
# 得到验证码在整个截图中的位置
angle=(
    int(location['x']*1.25),int(location['y']*1.25),int(size['width']*1.25+location['x']*1.25),int(size['height']*1.25+location['y']*1.25)
)
i=Image.open('yzm.png')
# 定义截取后验证码图片名字
code_img='success.png'
# 截取验证码图片
frame=i.crop(angle)
# 保存
frame.save(code_img)
'''

# 利用超级鹰接口超级鹰识别
chaojiying = Chaojiying_Client('31415926qfz', '31415926qfz', '918548')
im = open('code.png', 'rb').read()
result=chaojiying.PostPic(im, 9004)['pic_str']
print (chaojiying.PostPic(im, 9004)['pic_str'])

#对返回坐标进行处理
all_list=[]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)

    for k in range(count_1):
        xy_list=[]
        x=int(list_1[k].split(',')[0])
        y=int(list_1[k].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    xy_list = []
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])

    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)

for l in all_list:
    x=l[0]
    y=l[1]
    ActionChains(driver).move_to_element_with_offset(img_pos,x,y).click().perform()
    sleep(0.5)
u=driver.find_element_by_id('J-userName')
u.send_keys('q17633623606')
p=driver.find_element_by_id('J-password')
p.send_keys('1357abcd')
sleep(2)
login=driver.find_element_by_id('J-login')
login.click()








