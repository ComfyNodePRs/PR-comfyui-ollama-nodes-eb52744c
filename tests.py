from pull_model import PullModel

model_puller = PullModel()
model_puller.pull_model("phi3", "latest", stream=True)