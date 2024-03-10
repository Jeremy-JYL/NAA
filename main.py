import yaml, sys, random, webbrowser, datetime, sys, tqdm
from colorama import Fore

def chat(message, data):
    for i in data.values():
        if message.lower() in i["Triggers"]:
            if str(i["Responds"][0]).startswith("http://") or str(i["Responds"][0]).startswith("https://"):
                webbrowser.open(i["Responds"][0])
            elif str(i["Responds"][0]).startswith("time"):
                return datetime.datetime.now()
            elif str(i["Responds"][0]) == "code":
                print(Fore.RESET, end="")
                exec(i["Code"])
            else:
                return random.choice(i["Responds"])

if __name__ == "__main__":
    print("NAA - Not An AI")
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "data.yaml"
    with open(file, "r") as f:
        file_size = f.seek(0, 2)
        f.seek(0)
        bar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True, colour="BLUE")
        yaml_data = ''
        chunk_size = 1024
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yaml_data += chunk
            bar.update(len(chunk))
        data = yaml.safe_load(yaml_data)
        del yaml_data
        bar.close()
    print()
    while True:
        try:
            print(Fore.BLUE, end="")
            out = chat(input(""), data)
            if out:
                print(Fore.GREEN + f"NAA: {Fore.RESET + str(out)}")
        except KeyboardInterrupt:
            break
