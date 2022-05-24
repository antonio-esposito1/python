
#!/usr/bin/env python3.9

if __name__ == "__main__":
    import json
    with open("devices.json") as f:
        data = f.read()
        json_dict = json.loads(data)
        print("loaded as type {0}\n".format(type(json_dict)))
        print("items")
    for k, v in json_dict.items():
        print(" the key {0} contains a {1} value.".format(str(k), str(type(v))))