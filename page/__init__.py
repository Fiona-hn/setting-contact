
from selenium.webdriver.common.by import By


"""通讯录页面参数配置"""
# 添加联系人
Add_contact = By.ID, "com.android.contacts:id/floating_action_button"


"""新增联系人页面参数配置"""
# 姓名输入框
add_name = By.XPATH, "//*[@text='姓名']"
#  电话输入框
add_tel = By.XPATH, "//*[@text='电话']"


"""联系人详情页面参数配置"""
name = By.ID, "com.android.contacts:id/large_title"