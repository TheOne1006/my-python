#




## ENV

- appium
- Android Stadiuo
    - Android SDK Tool
- uiautomatorviewer
- adb shell


## 常用 shell


```shell
上传当前xml
adb pull /data/local/tmp/uidump.xml ./u.xml


# goto shell
 dumpsys window windows | grep -E 'mCurrentFocus'
```