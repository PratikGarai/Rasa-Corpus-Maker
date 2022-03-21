import requests
import json
import argparse

class Translator : 
    def __init__(self, key : str, region : str, lang : str) :
        self.key = key
        self.region = region
        self.URL = f"api.cognitive.microsofttranslator.com/translator/text/v3.0/translate?to={lang}"
        self.headers = {
            "Ocp-Apim-Subscription-Key" : self.key,
            "Ocp-Apim-Subscription-Region" : self.region,
            "Content-Type" : "application/json"
        }
    
    def translate(self, data : str) -> str:
        payload = {
            "Text" : data
        }
        r = requests.post(self.URL, data=json.dumps(payload), headers=self.headers)
        print(r.json())
        return data
    
    def test(self) :
        pass


def get_args() : 
    parser = argparse.ArgumentParser()
    parser.add_argument("--secret", type=str, help="name of your secret file")
    return parser.parse_args()

if __name__=="__main__" :
    t = Translator()
