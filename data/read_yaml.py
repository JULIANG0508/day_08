import os

import yaml

list = []
print(os.getcwd())

with open("./data.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(data)

    for i in data.values():
        # print(i)
        # print(i.values())

        list.append((i.get("input"), i.get("exp")))

    print(list)
