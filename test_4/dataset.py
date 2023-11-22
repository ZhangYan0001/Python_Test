from paddlehub.datasets.base_nlp_dataset import TextMatchingDataset

# 加载文本匹配任务 自定义数据集，继承TextMatchingDataset类，替换数据集地址
class COVID19Competition(TextMatchingDataset):
  def __init__(self, tokenizer=None, max_seq_len=None):
    base_path = "Covid19Competition"
    super(COVID19Competition, self).__init__(
      is_pair_wise=False,
      base_path=base_path,
      train_file="train.tsv",
      dev_file="dev.tsv",
      train_file_with_header=True,
      dev_file_with_header=True,
      label_list=["0", "1"],
      tokenizer=tokenizer,
      max_seq_len=max_seq_len,
    )
