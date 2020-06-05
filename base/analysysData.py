import os

import yaml


class AnalysysData:
    @classmethod
    def get_yaml_data(self, name):
        with open("./data" + os.sep + name, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
