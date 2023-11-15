import zipfile

import os


def unzip_data(src_path, target_path):
  if not os.path.isdir(target_path):
    z = zipfile.ZipFile(src_path, "r")
    z.extractall(path=target_path)
    z.close()
  

unzip_data("./test.zip","./test")