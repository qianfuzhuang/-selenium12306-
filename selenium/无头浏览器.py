from selenium import webdriver
from time import sleep
# 无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions
# 实现无可视化界面操作
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver=webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
# 实现规避检测

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('http://www.baidu.com')
print(driver.page_source)
sleep(2)
driver.quit()
