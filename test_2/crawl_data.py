# 爬取 百度百科数据
import json
import re  # noqa: F401
import requests
import datetime  # noqa: F401
import os
from bs4 import BeautifulSoup


def crawl_wiki_data():
  """
  爬取百度百科中《乘风破浪的姐姐第二季》中嘉宾信息返回html
  """

  headers = {
      "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
  }

  url = "https://baike.baidu.com/item/乘风破浪的姐姐第二季"

  try:
    response = requests.get(url, headers)

    # 将一段文档传入BeautifulSoup的构造方法，就能得到一个文档的对象，可以传入一段字符串
    soup = BeautifulSoup(response.text, "lxml")

    # print(soup)
    # 返回所有的<table>标签
    tables = soup.find_all("table")
    # print(tables)

    crawl_table_title = "嘉宾介绍"
    for table in tables:
      # table_titles = table.find("div")
      if crawl_table_title in table.text:
        return table

      # print(table_titles)
      # for title in table_titles:
      # print(title)
      # if (crawl_table_title in title):
      # return table

  except Exception as e:
    print(e)


# crawl_wiki_data()
# print(crawl_wiki_data())


def parse_wiki_data(table_html):
  """
    解析得到选手信息，包括选手姓名和选手个人百度百科页面链接，保存为Json文件，保存到work目录下
  """

  bs = BeautifulSoup(str(table_html), "lxml")
  all_trs = bs.find_all('tr')

  stars = []

  for tr in all_trs:

    if tr.find("td"):
      td = tr.find("td")

      if td.find("a"):
        star = {}

        if (td.find_next("a").text.isspace() is False):
          star["name"] = td.find_next("a").text
          star["link"] = "https://baike.baidu.com" + \
              td.find_next("a").get("href")
          stars.append(star)

  json_data = json.loads(str(stars).replace("\'", "\""))
  with open("./files/stars.json", "w", encoding="UTF-8") as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)
  # print(stars)


# table_html = crawl_wiki_data()
# parse_wiki_data(table_html)

def down_save_pic(name, pic_urls):
  path = "./files/imgs/" + name + "/"

  if not os.path.exists(path):
    os.makedirs(path)

  for i, pic_url in enumerate(pic_urls):
    try:
      pic = requests.get(pic_url, timeout=15)
      string = str(i + 1) + ".jpg"
      with open(path + string, "wb") as f:
        f.write(pic.content)
    except Exception as e:
      print(e)
      continue


def crawl_everyone_wiki_urls():
  with open("./files/stars.json", "r", encoding="UTF-8") as file:
    json_array = json.loads(file.read())

  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
  }

  star_infos = []

  for star in json_array:
    star_info = {}
    name = star["name"]
    link = star["link"]
    star_info["name"] = name

    response = requests.get(link, headers=headers)

    bs = BeautifulSoup(response.text, 'lxml')

    if bs.find("div", {"class": "basicInfo_IQmSj J-basic-info"}):
      base_info_div = bs.find("div", {"class": "basicInfo_IQmSj J-basic-info"})
      dls = base_info_div.find_all("dl")
    elif bs.find("div", {"class": "basicInfo_GgMeE J-basic-info"}):
      base_info_div = bs.find("div", {"class": "basicInfo_GgMeE J-basic-info"})
      dls = base_info_div.find_all("dl")
    elif bs.find("div", {"class": "basic-info J-basic-info cmn-clearfix"}):
      base_info_div = bs.find(
          "div", {"class": "basic-info J-basic-info cmn-clearfix"})
      dls = base_info_div.find_all("dl")
    else:
      continue

    for dl in dls:
      dts = dl.find_all("dt")

    # print(dts)
      for dt in dts:
        if "".join(str(dt.text).split()) == "民族":
          notion_str = str(dt.find_next("dd").text)
          star_info["nation"] = notion_str[0:notion_str.find("族")] + "族"

        if "".join(str(dt.text).split()) == "星座":
          star_str = str(dt.find_next("dd").text)
          star_info["constellation"] = star_str[0:star_str.find("座")]+ "座"

        if "".join(str(dt.text).split()) == "血型":
          blood_str = str(dt.find_next("dd").text)
          star_info["blood_type"] = blood_str[0:blood_str.find("型")] + "型"

        if "".join(str(dt.text).split()) == "身高":
          height_str = str(dt.find_next("dd").text)
          star_info["height"] = str(
              height_str[0:height_str.rfind('cm')]).replace("\n", "")

        if "".join(str(dt.text).split()) == "体重":
          weight_str = str(dt.find_next("dd").text)
          
          star_info["weight"] = weight_str[0:weight_str.rfind("k")]

        if "".join(str(dt.text).split()) == "出生日期":
          birth_day_str = str(dt.find_next("dd").text)
          if "年" in birth_day_str:
            star_info["birth_day"] = birth_day_str[0:birth_day_str.find("年")]

    star_infos.append(star_info)
  # 图片爬取，遇到困难，回头再看
  # print(star_infos)
    # img_a_all = bs.find_all("a", {"class": "albumWrapper_s7ocg"})
    # pic_list_url :str
    # if img_a_all:
    #   for img_a in img_a_all:
    #     print(img_a.get("title"))
    #     if name in str(img_a.get("title")):
    #       pic_list_url = img_a.get("href")
    #       break

    # # if bs.select(".albumWrapper_s7ocg"):
    # # pic_list_url =  bs.select(".albumWrapper_s7ocg")[0].get("href")
    # # print(pic_list_url)
    # pic_list_url = "https://baike.baidu.com" + pic_list_url

    # # print(pic_list_url)
    # if requests.get(pic_list_url,headers):
    #   pic_list_response = requests.get(pic_list_url, headers=headers)
    #   bs = BeautifulSoup(pic_list_response.text, "lxml")
    #   pic_list_html = bs.select(".pic-list img")
    # pic_urls = []

    # for pic_html in pic_list_html:
    #   pic_url = pic_html.get("src")
    #   pic_urls.append(pic_url)

    # down_save_pic(name, pic_urls)

  json_data = json.loads(str(star_infos).replace(
      "\'", "\"").replace("\\xa0", ""))
  with open("./files/stars_info.json", "w", encoding="UTF-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)


crawl_everyone_wiki_urls()
