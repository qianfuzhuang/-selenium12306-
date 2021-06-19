from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver=webdriver.Chrome()

driver.get(url)
# 如果存在iframe标签之中要切换标签定位作用域
driver.switch_to.frame('iframeResult')
div=driver.find_element_by_id('draggable')
# 动作链
action=ActionChains(driver)
# 点击长按指定标签
action.click_and_hold(div)
for i in range(5):
    action.move_by_offset(17,0).perform()
    sleep(0.3)
action.release()
driver.quit()