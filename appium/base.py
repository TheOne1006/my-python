# Android environment
from appium import webdriver
from time import sleep

realDevice = '5652ca21'


desired_caps = dict(
    platformName='Android',
    platformVersion='7.1.2',
    automationName='uiautomator2',
    deviceName=realDevice,
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps )


# print(driver.context)
print('计算器是否安装 %s ' % driver.is_app_installed('com.miui.calculator'))
driver.back()

sleep(2)

# 这里第一个参数是要启动的Activity的包名，第二个参数是要启动的Activity名
# driver.find_element_by_accessibility_id('com.miui.calculator:id/digit_1').click()
# adb -s 5652ca21 shell
# dumpsys window windows | grep -E 'mCurrentFocus' 查找当前
# mCurrentFocus=Window{6850306 u0 com.miui.calculator/com.miui.calculator.cal.CalculatorActivity}
driver.start_activity('com.miui.calculator', 'com.miui.calculator.cal.CalculatorActivity')

sleep(2)


# 查找点击
driver.find_element_by_id('com.miui.calculator:id/digit_2').click()


# 描述
# driver.find_element_by_accessibility_id('com.miui.:id/digit_3').click()

# by text 3
driver.find_element_by_xpath("//*[@text='3']").click()


driver.get_screenshot_as_file('screenshot.png')