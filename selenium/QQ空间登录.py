from selenium import webdriver

from time import sleep

url='https://qzone.qq.com/'
driver=webdriver.Chrome()
driver.get(url)
driver.switch_to.frame('login_frame')
cli=driver.find_element_by_id('switcher_plogin')
cli.click()
user=driver.find_element_by_id('u')
user.send_keys('469422624')
sleep(2)
pass_w=driver.find_element_by_id('p')
pass_w.send_keys('*')
sleep(2)
btn=driver.find_element_by_id('login_button')
btn.click()
sleep(5)


