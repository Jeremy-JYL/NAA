import yaml
import random
import webbrowser
import datetime
import sys

def chat(message, data):
    for i in data.values():
        if message.lower() in i["Triggers"]:
            if str(i["Responds"][0]).startswith("http://") or str(i["Responds"][0]).startswith("https://"):
                webbrowser.open(i["Responds"][0])
            elif str(i["Responds"][0]).startswith("time"):
                return datetime.datetime.now()
            else:
                return random.choice(i["Responds"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "data.yaml"
    with open(file, "r") as f:
        data = yaml.safe_load(f.read())
    while True:
        try:
            out = chat(input("NAA> "), data)
            if out:
                print(out)
        except KeyboardInterrupt:
            break
