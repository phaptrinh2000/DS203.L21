import yaml
from data_process.data_process import data_process

config = yaml.safe_load(open('/content/DS203.L21/CapsNet/config.yml'))

data_process(config)
