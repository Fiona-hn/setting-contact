from appium import webdriver


def get_driver():
    # 保存变量字典
    desired_caps = dict()
    # 手机参数配置
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 可输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 不重置应用
    desired_caps['noReset'] = True
    # 应用参数：包名和界面名 - 联系人
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

