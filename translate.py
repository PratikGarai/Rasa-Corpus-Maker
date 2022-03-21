import argparse

def get_args() : 
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", type=str, required=True, help="path to your train dataset"
    )
    parser.add_argument("--name", type=str, help="name of your save file")
    return parser.parse_args()

if __name__=="__main__" :
    args = get_args()