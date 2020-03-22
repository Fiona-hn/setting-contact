from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def base_get_element(self, requre, timeout=30, poll=0.5):
        method_by, value = requre
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(method_by, value))

    # 点击 事件
    def base_click(self, loc):
        self.base_get_element(loc).click()

    # 输入内容 事件
    def base_input(self, loc, value):
        el = self.base_get_element(loc)
        # 清除内容
        el.clear()
        # 输入内容
        el.send_keys(value)

    # 点击手机返回键
    def base_press_back(self):
        self.driver.press_keycode(4)

    # 获取文本
    def base_get_text(self, loc):
        return self.base_get_element(loc).text
    
