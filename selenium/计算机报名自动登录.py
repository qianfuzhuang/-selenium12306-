from selenium import webdriver
from time import sleep
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




url='https://passport.neea.cn/NCRELogin?ReturnUrl=https://ncre-bm.neea.cn/Home/VerifyPassport/?LoginType=0|41&Safe=1'
driver=webdriver.Chrome()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})


sleep(1)
driver.get(url)
user=driver.find_element_by_id('txtUserName')
user.send_keys('账号')

pass_w=driver.find_element_by_id('txtPassword')
pass_w.send_keys('密码')
sleep(0.1)

driver.find_element_by_xpath(
    '//*[@id="imgCheckImage"]').screenshot('./comp.png')

chaojiying = Chaojiying_Client('超级鹰账号', '超级鹰密码', '918548')
im = open('comp.png', 'rb').read()
result=chaojiying.PostPic(im, 1902)['pic_str']
print (chaojiying.PostPic(im, 1902)['pic_str'])

code=driver.find_element_by_id('txtCheckImageValue')
code.send_keys(result)
sleep(1)
btn=driver.find_element_by_id('ibtnLogin')
btn.click()