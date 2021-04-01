from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.baidu.com/')


cookies = driver.get_cookies()

print(cookies)
# driver.add_cookie()

time.sleep(3)

# 退出模拟浏览器 避免残留进程
driver.quit()