#!/usr/bin/python3.9

if __name__== "__main__":
    import json
    with open("elenco.json") as f:
        data = f.read()
    json_dict = json.loads(data)
    for k, v in json_dict.items():
        print(" key {0} contain {1}".format(str(k), str(v)))

