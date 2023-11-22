import paddlehub as hub
import paddle
from dataset import COVID19Competition

hub.server_check()

model = hub.Module(name="ernie_tiny", version="2.0.2", task="text-matching")

# inputs, outputs, program = module.context(trainable=True, max_seq_len=128, num_slots=2)
# tokenizer = hub.BertTokenizer(tokenize_chinese_chars=True)
train_dataset = COVID19Competition(tokenizer=model.get_tokenizer(), max_seq_len=128, mode="train")
dev_dataset = COVID19Competition(tokenizer=model.get_tokenizer(), max_seq_len=128, mode="dev")
test_dataset = COVID19Competition(tokenizer=model.get_tokenizer(), max_seq_len=128, mode="test")

# 选择优化策略和运行配置
# 适用于ERNIE/BERT这类Transformer模型的迁移优化策略为AdamWeightDecayStrategy
# train_dataset = LCQMC(tokenizer=model.get_tokenizer(), max_seq_len=128, mode='train')
# dev_dataset = LCQMC(tokenizer=model.get_tokenizer(), max_seq_len=128, mode='dev')
# test_dataset = LCQMC(tokenizer=model.get_tokenizer(), max_seq_len=128, mode='test')
# strategy = hub.AdamWeightDecayStrategy(
#   weight_deacy=0.01,
#   warmup_proportion=0.1,
#   learning_rate=5e-5,
# )

# config = hub.RunConfig(
#   eval_interval=300,
#   num_epoch=3,
#   batch_size=32,
#   checkpoint_dir="ckpt_ernie_pointwise_matching",
#   strategy=strategy,
# )
optimizer = paddle.optimizer.AdamW(learning_rate=5e-5, parameters=model.parameters())
trainer = hub.Trainer(model, optimizer, checkpoint_dir="./")


# 模型训练
trainer.train(
  train_dataset=train_dataset,
  epochs=10,
  batch_size=32,
  eval_dataset=dev_dataset,
  save_interval=2,
)

trainer.evaluate(test_dataset, batch_size=32)
# query = outputs["sequence_output"]
# title = outputs["sequence_output_2"]


# pointwise_matching_task = hub.PointwiseTextMatchingTask(
#   dataset=dataset,
#   # query_feature=query,
#   # title_feature=title,
#   tokenizer=tokenizer,
#   config=config,
# )

# run_states = pointwise_matching_task.finetune_and_eval()


# paddle.save(model.state_dict(), str(epoch) + "_model_final.pdarams")
# paddle.save(model)
data = [
  ["这个表情叫什么", "这个猫的表情叫什么"],
  ["什么是智能手环", "智能手环有什么用"],
  ["介绍几本好看的都市异能小说，要完结的！", "求一本好看点的都市异能小说，要完结的"],
  ["一只蜜蜂落在日历上（打一成语）", "一只蜜蜂停在日历上（猜一成语）"],
  ["一盒香烟不拆开能存放多久？", "一条没拆封的香烟能存放多久。"],
]
label_map = {0: "similar", 1: "dissimilar"}

model = hub.Module(
  name="ernie_tiny",
  version="2.0.2",
  task="text-matching",
  load_checkpoint="./checkpoint/best_model/model.pdparams",
  label_map=label_map,
)
results = model.predict(data, max_seq_len=128, batch_size=1, use_gpu=True)
for idx, texts in enumerate(data):
  print("TextA: {}\tTextB: {}\t Label: {}".format(texts[0], texts[1], results[idx]))
