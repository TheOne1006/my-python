from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
# 设置等待执行语句
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.implicitly_wait(10)  # 隐式等待
driver.get(r'http:\\www.douban.com')

try:
    element = WebDriverWait(driver, 10).until(
        # 位于...位置存在某个元素
        # EC.presence_of_element_located((By.ID, 'form_email'))  # 必须是元组
        EC.text_to_be_present_in_element(
            (By.XPATH, '//div[@class="main"]/div[@class="mod"]/h2[1]'),
            '热点内容  • • • • • •  ( 更多 )')
    )
    # element.send_keys('python')
    print(element)
finally:
    driver.quit()