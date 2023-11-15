# 基于 Word2vecc 的语言模型实践
import requests
import random
import math
import numpy as np

# 下载语料用来训练


def download(file_path):
  corpus_url = "https://dataset.bj.bcebos.com/word2vec/text8.txt"

  web_request = requests.get(corpus_url)

  corpus = web_request.content
  with open(file_path, "wb") as f:
    f.write(corpus)

  f.close()
  return corpus


# 对语料库进行预处理（分词）
def data_preprocess(corpus:str):
  corpus = corpus.strip().lower()
  corpus = corpus.split(" ")
  return corpus


def build_dict(corpus):
  word_freq_dict = dict()

  # 统计每个不同词的词频，
  for word in corpus:
    if word not in word_freq_dict:
      word_freq_dict[word] = 0
    word_freq_dict[word] += 1

  # 排序，按照出现次数排序，次数越高，
  word_freq_dict = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)

  # 构造3个不同的词典，分别存储，每个词到id的映射关系：word2id_dict;
  # 每个id出现的频率：word2id_freq;
  # 每个id到词典映射关系：id2word_dict;
  word2id_dict = dict()
  word2id_freq = dict()
  id2word_dict = dict()

  # 按照频率，从高到低，开始遍历每个单词，并为这个单词构造一个独一无二的id
  for word, freq in word_freq_dict:
    curr_id = len(word2id_dict)
    word2id_dict[word] = curr_id
    word2id_freq[word2id_dict[word]] = freq
    id2word_dict[curr_id] = word

  return word2id_freq, word2id_dict, id2word_dict


def convert_corpus_to_id(corpus, word2id_dict):
  corpus = [word2id_dict[word] for word in corpus]
  return corpus

def subsampling(corpus, word2id_freq):
  # 这个函数决定了一个次会不会被替换，这个函数是具有随机性的，每次调用结果不同
  # 如果一个次的频率很大，那么它被抛弃的概率就很大
  def discard(word_id):
    return random.uniform(0, 1) < 1 - math.sqrt(1e-4 / word2id_freq[word_id] * len(corpus))

  corpus = [word for word in corpus if not discard(word)]
  return corpus


def build_data(corpus, word2id_dict, word2id_freq, max_window_size=3, negative_sample_num=4):
  dataset = []
  center_word_idx = 0
  vocab_size = len(word2id_freq)

  while center_word_idx < len(corpus):
    windows_size = random.randint(1, max_window_size)
    positive_word = corpus[center_word_idx]

    context_word_range = (
      max(0, center_word_idx - windows_size),
      min(len(corpus) - 1, center_word_idx + windows_size),
    )
    context_word_cndidates = [
      corpus[idx]
      for idx in range(context_word_range[0], context_word_range[1] + 1)
      if idx != center_word_idx
    ]

    for context_word in context_word_cndidates:
      dataset.append((context_word, positive_word, 1))

      i = 0
      while i < negative_sample_num:
        negative_word_candidate = random.randint(0, vocab_size - 1)

        if negative_word_candidate is not positive_word:
          dataset.append((context_word, negative_word_candidate, 0))
          i += 1

    center_word_idx = min(len(corpus) - 1, center_word_idx + windows_size)
    if center_word_idx == (len(corpus) - 1):
      center_word_idx += 1
    if center_word_idx % 10000 == 0:
      print(center_word_idx)

  return dataset


def build_batch(dataset, batch_size, epoch_num):
  center_word_batch = []
  target_word_batch = []

  label_batch = []

  for epoch in range(epoch_num):
    random.shuffle(dataset)

    for center_word, target_word, label in dataset:
      center_word_batch.append([center_word])
      target_word_batch.append([target_word])
      label_batch.append(label)

      if len(center_word_batch) == batch_size:
        yield (
          np.array(center_word_batch).astype("int64"),
          np.array(target_word_batch).astype("int64"),
          np.array(label_batch).astype("float32"),
        )
        center_word_batch = []
        target_word_batch = []
        label_batch = []

  if len(center_word_batch) > 0:
    yield (
      np.array(center_word_batch).astype("int64"),
      np.array(target_word_batch).astype("int64"),
      np.array(label_batch).astype("float32"),
    )


