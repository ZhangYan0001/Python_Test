from mimetypes import init
from paddle.distributed.auto_parallel.random import init_auto_parallel_rng
import paddle.nn


class SkipGram(paddle.nn.Layer):
  def __init__(self, vocab_size, embedding_size, init_scale=0.1):
    super(SkipGram, self).__init__()

    self.vocab_size = vocab_size
    self.embedding_size = embedding_size

    self.embedding = paddle.nn.Embedding(
      self.vocab_size,
      self.embedding_size,
      weight_attr=paddle.ParamAttr(
        name="embedding_para",
        initializer=paddle.nn.initializer.Uniform(
          low=-0.5 / embedding_size, high=0.5 / embedding_size
        ),
      ),
    )

    self.embedding_out = paddle.nn.Embedding(
      self.vocab_size,
      self.embedding_size,
      weight_attr=paddle.ParamAttr(
        name="embedding_out_para",
        initializer=paddle.nn.initializer.Uniform(
          low=-0.5 / embedding_size, high=0.5 / embedding_size
        ),
      ),
    )

  def forward(self, center_words, target_words, label):
    center_words_emb = self.embedding(center_words)
    target_words_emb = self.embedding_out(target_words)

    word_sim = paddle.multiply(center_words_emb, target_words_emb)
    word_sim = paddle.sum(word_sim, axis=-1)
    word_sim = paddle.reshape(word_sim, shape=[-1])
    
    pred = paddle.nn.functional.sigmoid(word_sim)

    loss = paddle.nn.functional.binary_cross_entropy(paddle.nn.functional.sigmoid(word_sim), label)
    loss = paddle.mean(loss)
    return pred, loss
