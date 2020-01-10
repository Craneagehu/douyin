from appium import webdriver
#WebDriverWait用来加入时间判断，有时候控件元素需要过一段时间才会出现
from selenium.webdriver.support.ui import WebDriverWait
import time

#配置信息
option={
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    #自动化测试包名
    "appPackage": " com.ss.android.ugc.aweme",
    #自动化测试Activity
    "appActivity": "com.ss.android.ugc.aweme.following.ui.FollowRelationTabActivity",
    # #再次启动不需要再次安装
    # "noReset": True,
    # #unicode键盘 我们可以输入中文
    # "unicodekeyboard": True,
    # #操作之后还原回原先的输入法
    # "resetkeyboard":True
}

#其中的4723就是appium服务启动时的端口号
driver = webdriver.Remote("http://localhost:4723/wd/hub",option)

#放大镜按钮
# try:
#     #使用resource-id查找按钮
#     if WebDriverWait(driver,5).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/b3o')):
#         #点击按钮
#         driver.find_element_by_id('com.ss.android.ugc.aweme:id/b3o').click()
# except:
#     pass
