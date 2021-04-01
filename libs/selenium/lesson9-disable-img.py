from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()
num = str(float(random.randint(500, 600)))
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/{}"
                     " (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/{}".format(num, num))
# 禁止图片和css加载
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get('https://www.ly.com/')

time.sleep(5)


driver.quit()