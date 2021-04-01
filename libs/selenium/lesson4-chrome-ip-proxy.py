from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

proxy = {'address': '103.151.47.114:8080'}


capabilities = dict(DesiredCapabilities.CHROME)
capabilities['proxy'] = {'proxyType': 'MANUAL',
                         'httpProxy': proxy['address'],
                         'ftpProxy': proxy['address'],
                         'sslProxy': proxy['address'],
                         'noProxy': '',
                         'class': "org.openqa.selenium.Proxy",
                         'autodetect': False}


chrome_options = Options()
# chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)


# driver.get('https://www.bfkdim.com/messages?phone=67402256')
driver.get('https://tool.lu/ip/')

# driver.execute_script('window.scrollTo(0, 223)')
# time.sleep(2)
#
# driver.execute_script('window.scrollTo(0, 1408)')

time.sleep(10)

# driver.save_screenshot('baidu.png')

print(driver.title)

# 退出模拟浏览器 避免残留进程

driver.quit()