import os
from jamdict import config as dictConfig
from jamdict import Jamdict
import argparse
import json


def lookup_dictionary(japanese_dictionary, kanji_lookup):
    dicResult = japanese_dictionary.lookup(kanji_lookup)
    for entry in dicResult.entries:
        print(entry.senses[0].gloss)


def load_japanese_dictionary(config_file):
    with open(config_file) as dict_config_file:
        config_file_data = json.load(dict_config_file)

    dictConfig.__app_config.config['JAMDICT_HOME'] = config_file_data['JAMDICT_HOME']
    dictConfig.__app_config.config['JAMDICT_DATA'] = config_file_data['JAMDICT_DATA']
    dictConfig.__app_config.config['JAMDICT_DB'] = config_file_data['JAMDICT_DB']
    dictConfig.__app_config.config['JMDICT_XML'] = config_file_data['JMDICT_XML']
    dictConfig.__app_config.config['JMNEDICT_XML'] = config_file_data['JMNEDICT_XML']
    dictConfig.__app_config.config['KD2_XML'] = config_file_data['KD2_XML']
    dictConfig.__app_config.config['KRADFILE'] = config_file_data['KRADFILE']
    # print(dictConfig.__app_config.config)

    jmdict = Jamdict()

    return jmdict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='script.py')
    parser.add_argument('-c', default=f'{os.path.dirname(__file__)}/../japanesedict/config.json', help='Config file '
                                                                                                       'containaing '
                                                                                                       'dict '
                                                                                                       'locations.')
    # parser.add_argument('-f', required=True, help='File containing the kanji list.')
    args = parser.parse_args()
    japanese_dictionary = load_japanese_dictionary(args.c)
    lookup_dictionary(japanese_dictionary, u'今日')
