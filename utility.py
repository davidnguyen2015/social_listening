import configparser
import os

def get_config(key):
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__) + '/config.ini')

    if 'config' not in config:
        raise Exception("Section 'config' not found in config.ini.")
        
    return config.get('config', key)