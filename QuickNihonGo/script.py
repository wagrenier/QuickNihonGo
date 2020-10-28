import os
from jamdict import config as dictConfig
from jamdict import Jamdict
import argparse

dictConfig.__app_config.config['JAMDICT_HOME'] = f'{os.path.dirname(__file__)}/../japanesedict'
print(dictConfig.__app_config.config)

jmdict = Jamdict()

r = u'今日'
dicResult = jmdict.lookup(r)

for entry in dicResult.entries:
     print(entry.senses[0].gloss)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='script.py')
    parser.add_argument('-c', required=True, help='Root folder containing the dict data folder.')
    args = parser.parse_args()