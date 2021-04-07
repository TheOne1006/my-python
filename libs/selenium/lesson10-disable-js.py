# 没有成功
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()
options.add_argument('--host-rules=MAP" *.*.* 127.0.0.1"')
# options.add_argument('--host-resolver-rules=MAP www.googletagmanager.com 127.0.0.1')


driver = webdriver.Chrome(options=options)

driver.get('https://www.bfkdim.com/messages?phone=17043542312')

time.sleep(5)


# driver.quit()