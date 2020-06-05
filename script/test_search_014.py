import pytest
from base.analysysData import AnalysysData
from base.driver import Driver
from base.page import Page



def get_data():
    data_list = []

    data = AnalysysData.get_yaml_data("data.yaml")

    for i in data.values():
        # print(i)
        # print(i.values())

        data_list.append((i.get("input"), i.get("exp")))

    return data_list


class TestSearch:

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.fixture(scope="class", autouse=True)  # 因为只点击一次搜索按钮 自动运行
    def click_search_btn(self):
        """点击搜索按钮 1次 输入之前运行"""
        # 点击搜索
        Page.get_page_shezhi().click_sousuobut()

    @pytest.mark.parametrize("search_text,search_result", get_data())
    def test_search(self, search_text, search_result):
        """内容输入 和 结果断言"""
        # 输入框
        Page.get_page_sousuo().input_text(search_text)

        # 断言 -列表式断言
        assert search_result in Page.get_page_sousuo().get_result()
