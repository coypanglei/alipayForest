from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.touch_actions import TouchActions
from subprocess import Popen, PIPE
from Alipay import TEMP_FILE, TEMP_FILE_TWO, matchImg

server = 'http://localhost:4723/wd/hub'


class AlipayLogin():
    def __init__(self):
        # 查看当前的devices
        self.adb_devices = r"adb devices"
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'abb2c20e9904',
            'udid': 'abb2c20e9904',
            'appPackage': 'com.eg.android.AlipayGphone',
            'appActivity': '.AlipayLogin',
            'newCommandTimeout': "2000",
            'unicodeKeyboard': False,
            'resetKeyboard': False,
            'noReset': True,
        }

    def gohome(self):
        self.num = 0
        id = self.getDevices()
        self.desired_caps['deviceName'] = id
        self.desired_caps['udid'] = id
        self.driver = webdriver.Remote(server, self.desired_caps)
        # 执行命令等待的时间
        self.wait = WebDriverWait(self.driver, 20)
        self.Action = TouchActions(driver=self.driver)

        sleep(5)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@text="蚂蚁森林"]'))).click()
        sleep(5)
        print(self.driver.page_source)
        chakanfriend = self.driver.find_element_by_xpath(
            '//*[@content-desc="查看更多好友"]')
        print(chakanfriend.size)
        print(chakanfriend.size['height'])
        self.swipe_up(0, chakanfriend.size['height'])
        chakanfriend.click()
        sleep(5)
        print(self.driver.page_source)
        # 保存图片
        if self.driver.save_screenshot(TEMP_FILE):
            rectangle = matchImg(TEMP_FILE, TEMP_FILE_TWO, 0.99)
            circle_center_pos = rectangle['rectangle']
            print(circle_center_pos)
            self.driver.tap([circle_center_pos[0], circle_center_pos[3]], 100)

    def getDevices(self):
        devices = Popen(self.adb_devices, shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
        print(devices)
        # 删掉第一个元素
        del devices[0]
        for i in devices:
            i = i.decode('utf-8')
            if i.find("device") > 0:
                i = i.split()[0]
                return i

    # 屏幕宽高
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # def swipe_up(self, t=0):
    #     screen = self.get_size()
    #     self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.5, t)

    def swipe_up(self, t=0, y=0):
        screen = self.get_size()
        y = y - screen[1]
        while y < 0:
            self.driver.swipe(screen[0] * 0.5, screen[1] * 0.75, screen[0] * 0.5, screen[1] * 0.25, t)
            y = y + screen[1] * 0.25

    def swipe_down(self, t=0):
        screen = self.get_size()
        self.driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, t)


if __name__ == "__main__":
    alipay = AlipayLogin()
    # try:
    alipay.gohome()
    # except Exception as e:
    #     print(e)
