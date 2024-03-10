import yaml, sys, random, webbrowser, datetime, sys, tqdm
from colorama import Fore

# Add Learning support
def learn(t, r):
    if r != "":
        data.append({"Triggers": [t], "Responds": r.split("`~`")})

# Main Chat Function
def chat(message, data):
    if message:
        for i in data:
            if message.lower() in i["Triggers"]:
                if str(i["Responds"][0]).startswith("http://") or str(i["Responds"][0]).startswith("https://"):
                    webbrowser.open(i["Responds"][0])
                elif str(i["Responds"][0]).startswith("time"):
                    return datetime.datetime.now()
                elif str(i["Responds"][0]) == "code":
                    print(Fore.RESET, end="")
                    exec(i["Code"])
                    print()
                    return
                else:
                    return random.choice(i["Responds"])
        learn(message.lower(), input("Responds ('`~`' New Items): "))


if __name__ == "__main__":
    print("NAA - Not An AI")
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "data.yaml"
    # Loading Files
    with open(file, "r") as f:
        file_size = f.seek(0, 2)
        f.seek(0)
        bar = tqdm.tqdm(total=file_size, unit='B', unit_scale=True, colour="BLUE")
        yaml_data = ''
        chunk_size = 1024
        # Progress Bar
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yaml_data += chunk
            bar.update(len(chunk))
        data = list(yaml.safe_load(yaml_data).values())
        del yaml_data
        bar.close()
    print()
    # Chatting UI
    while True:
        try:
            print(Fore.BLUE + "You: " + Fore.RESET, end="")
            out = chat(input(), data)
            if out:
                print(Fore.GREEN + f"NAA: {Fore.RESET + str(out)}")
        except KeyboardInterrupt:
            break
