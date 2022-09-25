import yaml

config = {}

with open('backlog/config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)