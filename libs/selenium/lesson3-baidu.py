from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.baidu.com')


driver.find_element_by_id('kw').send_keys('python')

time.sleep(1)

driver.find_element_by_id('su').click()

time.sleep(6)

# 退出模拟浏览器 避免残留进程
driver.quit()