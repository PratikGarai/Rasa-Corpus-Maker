import argparse
import yaml
from yaml.loader import SafeLoader
import pprint
import json


class Translator : 
    def __init__(self) :
        pass 
    
    def translate(self, data : str) -> str:
        return data


class TranslatorDriver : 
    def __init__(self, infile_name : str, outfile_name : str) :
        with open(infile_name) as f:
            self.data = yaml.load(f, Loader=SafeLoader)
        self.outfile_name = outfile_name
        self.translator = Translator()
        self.res = {}


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
                d.append(self.translator.translate(dialogue))
            conversations.append(d)
        res["conversations"] = conversations
        self.res = res



def get_args() : 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", type=str, required=True, help="path to your train dataset"
    )
    parser.add_argument("--name", type=str, help="name of your save file")
    return parser.parse_args()

if __name__=="__main__" :
    args = get_args()
    t = TranslatorDriver(args.data, args.name)
    t.print_result()