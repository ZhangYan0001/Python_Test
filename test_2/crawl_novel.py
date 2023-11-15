import json
# from urllib import response
import requests

from bs4 import BeautifulSoup
import os  # noqa: F401

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

url_top = "https://biquchi.com/"
url = "https://biquchi.com/book/2517.html"

novel_detail = {}


def crawl_novel_detail(url, header) -> {}:
  try:

    name = ""
    detail = ""
    response = requests.get(url, headers=header)  # noqa: F811

    bs = BeautifulSoup(response.text, "lxml")
    div_top = bs.find("div", {"class": "stui-pannel-box"})

    detail_div = div_top.find_next("div", {"class": "stui-content__detail"})
    contents = detail_div.contents
    for content in contents:
      if content.find_next("h1"):
        name = " " + str(content.find_next("h1").next) + " "
      else:
        detail += str(content.text).replace(u"\xa0",
                                            u"").replace("\n", "") + " "
    return {"name": name, "detial": detail}

  except Exception as e:
    print(e)


# novel_detail = crawl_novel_detail(url, header)
# print(novel_detail)


# def crawl_capter_list(url, header) -> []:
#   capter_list = []

#   try:
#     response = requests.get(url, headers=header)
#     bs = BeautifulSoup(response.text, "lxml")

#     capter_list_div = bs.find("div", {"class": "stui-pannel_bd"})
#     capters = capter_list_div.find_next("ul").find_all("li")
#     # print(capters)

#     for capter in capters:
#       index = ""
#       href = ""
#       a_tag = capter.find_next("a")
#       index = str(a_tag.text)
#       href = url_top + str(a_tag.get("href"))
#       capter_list.append({"index": index, "href": href})

#     return capter_list
#   except Exception as e:
#     print(e)
def crawl_capter_list(url, header) -> []:
  capter_list = []
  url_ = "https://www.bige3.cc/"

  try:
    response = requests.get(url, headers=header)  # noqa: F811
    bs = BeautifulSoup(response.text, "lxml")

    capter_list_div = bs.find("div", {"class": "listmain"})
    capters = capter_list_div.find_all("dd")
    # print(capters)

    for capter in capters:
      index = ""
      href = ""

      a_tag = capter.find_next("a")
      index = str(a_tag.text)
      href = url_ + str(a_tag.get("href"))
      capter_list.append({"index": index, "href": href})

    return capter_list
  except Exception as e:
    print(e)

# lists = crawl_capter_list("https://www.bige3.cc/book/8971/",header=header)
# for list in lists:
#   print(list)


def capter_list_to_json(capter_list: []):
  json_data = json.loads(str(capter_list).replace("\'", "\""))
  with open("./files/capter_list2.json", "w", encoding="UTF-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)


# capter_list_to_json(crawl_capter_list("https://www.bige3.cc/book/8971/", header))


# def download_novel(json_file_name: str, header):
#   try:

#     file_name = "./files/novel2.txt"
#     fd = open(file_name,"w",encoding="UTF-8")
#     fd.write("")
#     with open(json_file_name, "r", encoding="UTF-8") as file:
#       capter_list = json.loads(file.read())

#     # novel_str = ""
#     for capter in capter_list:
#       index = capter["index"]
#       href = capter["href"]

#       response = requests.get(href, headers=header)
#       bs = BeautifulSoup(response.text, "html.parser")
#       content = bs.find("div", {"class": "content"})

#       with open(file_name, "a", encoding="UTF-8") as novel_file:
#         novel_file.write("\n" + index + "\n" + "\n" + str(content.text).strip() + "\n")

#   except Exception as e:
#     print(e)

def download_novel(json_file_name: str, header):
  try:

    file_name = "./files/novel2.txt"
    fd = open(file_name,"w",encoding="UTF-8")
    fd.write("")
    with open(json_file_name, "r", encoding="UTF-8") as file:
      capter_list = json.loads(file.read())

    for capter in capter_list:
      index = capter["index"]
      href = capter["href"]

      response = requests.get(href, headers=header)  # noqa: F811
      bs = BeautifulSoup(response.text, "html.parser")
      content = bs.find("div",{"class":"Readarea"})


      with open(file_name, "a", encoding="UTF-8") as novel_file:
        novel_file.write("\n" + index + "\n" + "\n" + str(content.text).strip() + "\n")

  except Exception as e:
    print(e)

download_novel("./files/capter_list2.json", header)
