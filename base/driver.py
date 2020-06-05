import time

from appium import webdriver


class Driver:
    app_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.app_driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "android"
            desired_caps["platformVersion"] = "5.1"
            desired_caps["deviceName"] = "三星"
            desired_caps["appPackage"] = "com.android.settings"
            desired_caps["appActivity"] = ".Settings"
            cls.app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

            return cls.app_driver

        else:
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.app_driver is not None:
            time.sleep(5)
            cls.app_driver.quit()
            cls.app_driver = None
