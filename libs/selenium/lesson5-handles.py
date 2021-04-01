from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://bj.58.com/')

time.sleep(2)

# 点击打开 一个新标签
driver.find_elements_by_partial_link_text('租房')[2].click()

time.sleep(1)

# 获取所有标签页
wins = driver.window_handles

# 切换句柄
driver.switch_to.window(wins[1])


time.sleep(6)

# 退出模拟浏览器 避免残留进程
driver.quit()