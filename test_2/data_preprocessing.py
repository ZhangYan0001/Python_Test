from ast import increment_lineno  # noqa: F401
import matplotlib  # noqa: F401
import matplotlib.pyplot as plt# noqa: F401
import numpy as np# noqa: F401# noqa: F401
import json
import matplotlib.font_manager as font_manager# noqa: F401

# matplotlib inline

# 绘制 选手年龄分布柱状图，x为年龄，y轴为该年龄的数量

with open("./files/stars_info.json","r",encoding="UTF-8") as file:
  json_array = json.loads(file.read())

birth_days = []

for star in json_array:
  if "birth_day" in dict(star).keys():
    birth_day= star["birth_day"]
    if len(birth_day) == 4:
      birth_days.append(birth_day)

birth_days.sort()
print(birth_days)