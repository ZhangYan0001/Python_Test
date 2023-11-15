# 统计文件的类型与存储空间

import os

size_dict = {}
type_dict = {}
dirpath = "F:\\rust_advance\\rust_learning\\rustlings"


def get_size_type(path):
  # size_dict = {}
  # type_dict = {}
  files = os.listdir(path)
  for filename in files:
    temp_path = os.path.join(path, filename)
    if os.path.isdir(temp_path):
      get_size_type(temp_path)
    elif os.path.isfile(temp_path):
      type_name = os.path.splitext(temp_path)[1]
      if not type_name:
        type_dict.setdefault("None", 0)
        type_dict["None"] += 1
        size_dict.setdefault("None", 0)
        size_dict["None"] += os.path.getsize(temp_path)
      else:
        type_dict.setdefault(type_name, 0)
        type_dict[type_name] += 1
        size_dict.setdefault(type_name, 0)
        size_dict[type_name] += os.path.getsize(temp_path)


get_size_type(dirpath)

print("the size dict:", size_dict)
print("\n")
print("the type_dict:", type_dict)
print("\n")
