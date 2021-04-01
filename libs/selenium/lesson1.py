from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

print(driver.title)

# 退出模拟浏览器 避免残留进程

driver.quit()