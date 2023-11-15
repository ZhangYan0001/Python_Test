# 使用 Json 来存储数据
import json

numbers = [1, 2, 3, 4, 5]

filename = "./files/numbers.json"

# jump（），接受两个实参，要存储的数据以及可用于存储数据的文件对象。
with open(filename, "w") as f_obj:
  json.dump(numbers, f_obj)

# load(), 加载存储在numbers.json 中的信息
with open(filename) as f_obj:
  ns = json.load(f_obj)

print(ns)
