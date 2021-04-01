# Readme

- 相关文档
- 安装依赖
- 使用
   - driver
   - 定位
      - name,xpath,tag
   - 元素操作
      - 提取数据
      - 数据交互
   - 浏览器操作


## 文档

1. https://www.jianshu.com/p/78af96c883a5?from=singlemessage

2. in scrapy
    - https://blog.csdn.net/fox64194167/article/details/79914128
3. 启动参数
   - https://zhuanlan.zhihu.com/p/60852696
4. [异常速查](https://blog.csdn.net/yiwenrong/article/details/103800506)

## 环境安装


```shell
pip install selenium

# chrome driver
brew install chromedriver
```


### 基础



##### driver 对象常用属性方法

> 需要先实例化 deriver 对象

1. `driver.page_source` 当前标签页浏览器渲染之后的网页源代码
2. `driver.current_url` 当前url
3. `driver.close()` 关闭当前页面
4. `driver.quit()` 关闭浏览器
5. `driver.forward()` 前进
6. `driver.back()`
7. `driver.screen_shrt(img_name)` 截图
8. `driver.title`

#### 元素定位

1. `driver.find_element_by_id` 
2. `driver.find_element_by_class_name`
3. `driver.find_element_by_partial_link_text`
4. `driver.find_element_by_xpath`
5. `driver.find_element_by_css`


#### 元素操作

1. `element.text` 文本
2. `element.get_attribute(attrName)` 元素属性
3. `element.click()` 点击
4. `element.send_keys(value)` 模拟输入
5. `element.clear()` 清理元素内容
6. `element.submit()` 提交表单


#### 浏览器操作

1. 标签切换
   - 获取所有标签句柄
2. frame 切换
   - switch_to.frame(id)
   - switch_to.frame(index)
3. 获取 cookie
   - get_cookies
   - delete_cookie(cookieName)
   - delete_all_cookies()
   - add_cookies(cookie_dict) 
4. 页面等待
   - 等待机制
   - 强制等待 `time.sleep(3)`
   - 隐性等待 `driver.implicitly_wait(10)`
     - 加载完成立即执行下一步, 超出10s 也执行下一步
     - 只需要设置一次
   - 显性等待
     - 明确等待某一条件
    
5. 执行js
   - execute_script('jscode')
6. 无界面模式
   - `--headless`
   - `--disable-gpu`
7. ip 代理
8. user-agent

### 技巧

- ip代理
- 图片禁止加载


#### 1. ip 代理

postmane 设置 https://www.jianshu.com/p/fb3217eff97a


#### 2. 禁止图片和css加载

```python
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
options.add_experimental_option("prefs", prefs)
```

#### 3. ua

```python
chrome_options.add_argument('--user-agent=xxxx')
```