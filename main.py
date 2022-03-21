from rasa.shared.nlu.training_data.formats.rasa_yaml import RasaYAMLReader, RasaYAMLWriter
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
import yaml
from yaml.loader import SafeLoader
import pprint

class Solution : 
    def __init__(self) :
        self.data = {}
        self.result = {}
        self.yamlReader = RasaYAMLReader()
        self.yamlWriter = RasaYAMLWriter()

    def read_yml(self, fname : str) -> None :  
        with open(fname) as f:
            self.data = self.yamlReader.reads(f.read())

    def pretty_print_data(self) -> None : 
        pprint.pprint(RasaYAMLWriter.training_data_to_dict(self.data))
    
    def translate(self) -> None : 
        intents = self.data["nlu"]
        for intent in intents : 

            break

if __name__=="__main__":
    s = Solution()
    s.read_yml("src/inputs/nlu.yml")
    s.pretty_print_data()
