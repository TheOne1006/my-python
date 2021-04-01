from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.bfkdim.com/messages?phone=67402256')


driver.save_screenshot('baidu.png')

print(driver.title)

# 退出模拟浏览器 避免残留进程

driver.quit()