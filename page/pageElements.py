"""管理所有页面元素类"""
from selenium.webdriver.common.by import By


class PageElements:
    """建议：以页面为类 一个页面一个类"""

    """搜索页面类"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")

    """设置页面"""
    # 更多按钮
    setting_more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")

    """更多页面"""
    # 移动网络
    more_mobile_btn_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")

    """移动网络页面"""
    # 首选网络类型
    mobile_one_network_xpath = (By.XPATH, "//*[contains(@text,'首选网络类型')]")
    # 选择2G
    mobile_select_2G_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    # 获取页面所有描述信息
    mobile_summary_mess_ids = (By.ID, "android:id/summary")
