import argparse
import yaml
from yaml.loader import SafeLoader
import pprint
import json
import os

from src.utils.translator import Translator

class TranslatorDriver : 
    def __init__(self, infile_name : str, outfile_name : str, secret_name : str = None) :
        with open(infile_name) as f:
            self.data = yaml.load(f, Loader=SafeLoader)
        self.outfile_name = outfile_name
        self.secret_name = secret_name
        if self.secret_name : 
            self.load_secrets()
        self.translator = Translator(
            self.secrets["azure"]["key1"], 
            self.secrets["azure"]["region"], 
            "mr"
        )


    def print_data(self) :    
        pprint.pprint(self.data)


    def print_result(self) :    
        pprint.pprint(self.data)
    

    def process(self) :
        res = {}
        res["categories"] = self.data["categories"]

        conversations = []
        for conversation in self.data["conversations"] :
            d = []
            for dialogue in conversation : 
                # d.append(self.translator.translate(dialogue))
                d.append(dialogue)
            conversations.append(d)
        res["conversations"] = conversations
        self.res = res

    
    def load_secrets(self) :
        with open(self.secret_name) as f : 
            self.secrets = json.load(f)
    

    def save_result(self):
        with open(os.path.join("outputs", self.outfile_name+".yml"), 'w') as f:
            yaml.dump(self.res, f, sort_keys=False, default_flow_style=False)


def get_args() : 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", type=str, required=True, help="path to your train dataset"
    )
    parser.add_argument("--name", type=str, help="name of your save file")
    parser.add_argument("--secret", type=str, help="name of your secret file")
    return parser.parse_args()

if __name__=="__main__" :
    args = get_args()
    t = TranslatorDriver(args.data, args.name, args.secret)
    t.print_result()
    t.process()
    t.save_result()