import numpy as np
import paddle.optimizer
from Word2vec_model import convert_corpus_to_id, download,build_batch,build_data,build_dict,data_preprocess, subsampling
from skip_gram import SkipGram


batch_size = 512
epoch_num = 3
embedding_size = 200
step = 0
learning_rate = 0.001
file_path = r"F:\python_code\python_test\test_3\files\text8.txt"

corpus = download(file_path).decode("utf-8")
corpus = data_preprocess(corpus)

word2id_freq, word2id_dict, id2word_dict = build_dict(corpus)
# 将语料转换为id序列
corpus = convert_corpus_to_id(corpus,word2id_dict=word2id_dict)

# 使用二次采样算法（subsmpling)处理语料，强化训练效果 
corpus = subsampling(corpus=corpus,word2id_freq=word2id_freq)

vocab_size = len(word2id_freq)
print("there are totally %d different words in the corpus" % vocab_size)

for _, (word, word_id) in zip(range(50), word2id_dict.items()):
  print("word %s, its id %d, its word freq %d " % (word, word_id, word2id_freq[word_id]))

dataset = build_data(corpus, word2id_dict, word2id_freq)
for _, (context_word, target_word, label) in zip(range(50), dataset):
  print(
    "center_word %s , target %s , label %d "
    % (id2word_dict[context_word], id2word_dict[target_word], label)
  )

# build_batch(dataset,batch_size,epoch_num)


def get_cos(query1_token, query2_token, embed):
  W = embed
  x = W[word2id_dict[query1_token]]
  y = W[word2id_dict[query2_token]]
  cos = np.dot(x, y) / np.sqrt(np.sum(y * y) * np.sum(x * x) + 1e-9)
  # flat = cos.flatten()
  print("单词 1 %s 和单词2 %s 的cos结果为 %f" %(query1_token,query2_token,cos))

skip_gram_model = SkipGram(vocab_size,embedding_size)
adam = paddle.optimizer.Adam(learning_rate=learning_rate,parameters=skip_gram_model.parameters())

# 训练好了，测试一下
def test_word():
  embedding_matrix = np.load(r"F:\python_code\python_test\test_3\embedding.npy")
  get_cos("king", "queen", embedding_matrix)
  get_cos("she", "her", embedding_matrix)
  get_cos("topic", "theme", embedding_matrix)
  get_cos("woman", "game", embedding_matrix)
  get_cos("one", "name", embedding_matrix)
  get_cos("create", "delete", embedding_matrix)
  get_cos("test","content",embedding_matrix)


test_word()

# 开始训练
# # for center_words, target_words, label in build_batch(dataset,batch_size,epoch_num):
#   center_words_var = paddle.to_tensor(center_words)
#   target_words_var = paddle.to_tensor(target_words)

#   label_var = paddle.to_tensor(label)

#   pred, loss = skip_gram_model(center_words_var, target_words_var, label_var)

#   loss.backward()
  
#   adam.minimize(loss)
#   skip_gram_model.clear_gradients()

#   step += 1
#   if step % 100 == 0:
#     print("step %d, loss %.3f " %(step, loss.numpy()[0]))

#   if step %2000 == 0:
#     embedding_matrix = skip_gram_model.embedding.weight.numpy()
#     np.save("./embedding", embedding_matrix)
#     get_cos("king","queen",embedding_matrix)
#     get_cos("she","her",embedding_matrix)
#     get_cos("topic","theme",embedding_matrix)
#     get_cos("woman","game",embedding_matrix)
#     get_cos("one","name",embedding_matrix)




