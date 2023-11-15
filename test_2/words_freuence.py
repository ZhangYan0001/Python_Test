import jieba

# 打开文件
with open("./files/背影.txt", "r", encoding="UTF-8") as text_obj:
  texts = text_obj.read()


# 使用 jieba 分词
texts_list = list(jieba.lcut(texts))

# 中文停用词 统计
stopwords = [line.strip() for line in open(
    "./files/cn_stopwords.txt", "r", encoding="UTF-8").readlines()]


wordsDict = {}

for word in texts_list:
  if word is not stopwords:
    if len(word) == 1:
      continue
    else:
      wordsDict[word] = wordsDict.get(word, 0)+1


# 排序
wordsDictSorted = list(wordsDict.items())
wordsDictSorted.sort(key=lambda e: e[1], reverse=True)

topWordNum = 0
for topWordNum in wordsDictSorted[:20]:
  print(topWordNum)

# print(wordsDict)
