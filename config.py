import yaml

def load_config(config_file='/home/leonkemstach/prod/SYSTEMMONPROD/conf.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config
