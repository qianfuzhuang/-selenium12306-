
from selenium import webdriver
from lxml import etree
from time import sleep


url='http://scxk.nmpa.gov.cn:81/xk/'


driver=webdriver.Chrome(executable_path='./chromedriver')
driver.get(url)

# 标签定位
search_input=driver.find_element_by_id('')
# 标签交互
search_input.send_keys('')

# 执行一组js程序
js='window.scrollTo(0,document.body.scrollHeight)'
driver.execute_script('js')
sleep(2)

# 点击搜索按钮
btn=driver.find_element_by_css_selector('.btn-search')
btn.click()

# 回退
driver.back()
# 前进
driver.forward()








page_text=driver.page_source
# 解析
tree=etree.HTML(page_text)
li_list=tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    text=li.xpath('./i/@title')[0]
    print(text)
driver.close()