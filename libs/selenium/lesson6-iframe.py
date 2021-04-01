from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://qzone.qq.com/')


driver.switch_to.frame('login_frame')

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('12123')
driver.find_element_by_id('p').send_keys('12123123')
driver.find_element_by_id('login_button').click()



time.sleep(3)

# 退出模拟浏览器 避免残留进程
driver.quit()