import configparser
import os
import sys

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

appSetting = {
    'package': 'com.wudaokou.hippo',
    'indexPage': '.launcher.splash.SplashActivity',
    'loginPage': '.mine.MinePageActivity',
    'searchPage': 'com.wudaokou.hippo.search.SearchActivity',
    'loginForm': 'com.ali.user.mobile.login.ui.UserLoginActivity',
    'userPage': '.mine.MinePageActivity',
    'activePage': 'com.wudaokou.hippo.flutter.HMFlutterActivity'
}

config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(__file__), "..", "config.ini"))

platformVersion = config.get('androidDevices', 'phone1platformVersion')
phoneName = config.get('androidDevices', 'phone1uuid')
account = config.get('account', 'taobaoAccount')
password = config.get('account', 'taobaoPassword')

desired_caps = dict(
    platformName='Android',
    platformVersion=platformVersion,
    automationName='uiautomator2',
    deviceName=phoneName,
    appPackage=appSetting['package'],
    appActivity=appSetting['indexPage'],
    awaitActivity=appSetting['indexPage'],
    noReset=True,
    unicodeKeyboard=True,
    resetKeyboard=True
)

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

installed = driver.is_app_installed(appSetting['package'])

if not installed:
    print('未安装盒马 app')
    sys.exit(0)


def accountIsLogin():
    driver.find_element_by_xpath("//*[@text='我的']").click()

    driver.wait_activity(appSetting['userPage'], 15, 2)

    ua = driver.current_activity
    sleep(3)

    return ua == appSetting['userPage']

def loginAccount():
    driver.find_element_by_xpath("//*[@text='我的']").click()

    # driver.wait_activity('com.wudaokou.hippo.hybrid.webview.HMWebViewActivity', 5, 2)

    driver.wait_activity(appSetting['loginForm'], 15, 2)

    # driver.find_element_by_xpath("//*[@text='请输入淘宝账户']").send_keys(account)

    inputs = driver.find_elements_by_class_name("android.widget.EditText")

    # print(inputs)
    inputs[0].send_keys(account)
    inputs[1].send_keys(password)

    driver.find_element_by_accessibility_id("登录").click()


def goToMyTown():
    driver.find_element_by_xpath("//*[@text='盒马小镇']").click()
    driver.wait_activity('.category.WebNavigationActivity', 15, 2)
    sleep(5)

def tapMyflower():
    driver.wait_activity('.category.WebNavigationActivity', 10, 2)
    # ele = driver.find_element_by_xpath("//*[@text='任意消费']")
    # print('ele')
    # print(ele.touch())
    # sleep(3)
    # print('pre tap')
    # ele2 = driver.find_element_by_xpath("//*[@text='每日签到']")
    # print(ele2)
    sleep(5)
    driver.tap([(214,  596)], 300)
    sleep(3)

def goToOhterTown():
    sleep(3)
    try:
        driver.find_element_by_xpath("//*[@text='返回我的盒马小镇']")
        sleep(1)
        driver.tap([(617, 1003)], 300)
    except:
        driver.tap([(590, 788)], 500)
    sleep(1)

    # print('goto other town')
    # driver.tap([(590, 788)], 500)
    # sleep(3)

def tapOtherFlower():
    sleep(1)
    driver.tap([(241, 657)], 271)
    sleep(2)


is_login = True
    # accountIsLogin()

print(is_login)


try:
    if not is_login:
        print('需要登录')
        loginAccount()
    else:
        print('无需登录')

    goToMyTown()
    # tapMyflower()
    # goToOhterTown()
    # tapOtherFlower()

    for i in range(15):
        goToOhterTown()
        tapOtherFlower()
        sleep(2)

except:
    print('failed')

