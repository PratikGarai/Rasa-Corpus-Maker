import argparse
import yaml
from yaml.loader import SafeLoader
import pprint
import json
import os

from src.utils.translator import Translator

class YamlReaderPrinter : 
    def __init__(self, infile_name : str) :
        with open(infile_name) as f:
            self.data = yaml.load(f, Loader=SafeLoader)

    def print_data(self) :    
        pprint.pprint(self.data)


def get_args() : 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", type=str, required=True, help="path to file"
    )
    return parser.parse_args()

if __name__=="__main__" :
    args = get_args()
    t = YamlReaderPrinter(args.data)
    t.print_data()