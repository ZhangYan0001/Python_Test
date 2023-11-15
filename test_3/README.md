# 文本表示

## 基于 Word2vec 的语言模型实践

```py
# 简单的练习
# Time：2023.11.15
```

### 第一部分

数据处理在 Word2vec_model.py
其中包括：

```py
def download(file_path:str)

def data_preprocess(corpus:str)

def build_dict(corpus)

def convert_corpus_to_id(corpus, word2id_dict)

def subsampling(corpus, word2id_freq)

def build_data(corpus, word2id_dict, word2id_freq, 
max_windows_size = 3, negative_sample_num =4 )

def build_batch(dataset, batch_size, epoch_num)

```

### 第二部分

构建skip-gram模型

通过继承` paddle.nn.Layer ` 的类来搭建网络结构、参数的数据的声明

同时在forward函数中定义网络的计算逻辑

```py
class SkipGram(paddle.nn.Layer):
  def __init__()

  def fowrwad()

```

### 第三部分

模型训练

先定义一些超参数

```py

batch_size = 512
epoch_num = 3
embedding_size = 200
step = 0
learning_rate = 0.001
file_path = r"F:\python_code\python_test\test_3\files\text8.txt"

```

定义一个使用word-embedding 计算cos（）的函数

```py
def get_cos(query1_token, query2_token, embed):

```

开始训练
