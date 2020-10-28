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
     print(entry)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='script.py')
    parser.add_argument('-d', required=True, help='Repertoire contenant les sous-repertoires des auteurs')
    parser.add_argument('-a', help='Auteur a traiter')
    parser.add_argument('-A', action='store_true', help='Tous les auteurs')
    parser.add_argument('-f', help='Fichier inconnu a comparer') #Comparer avec un fichier random IMPLEMENTED
    parser.add_argument('-m', required=True, type=int, choices={1, 2}, help='Mode (1 ou 2) - unigrammes ou digrammes')
    args = parser.parse_args()