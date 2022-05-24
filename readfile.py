#!/usr/bin/python3.9

if __name__== "__main__":
    vlan_file = open('vlan.cfg', 'r')
    vlan_text = vlan_file.read()
    vlan_list = vlan_text.splitlines()
    vlans = []
    for item in vlan_list:
        if 'vlan' in item:
            temp = {}
            id = item.strip().strip('vlan').strip()
            temp['id'] = id
        elif 'name' in item:
            name = item.strip().strip('name').strip()
            temp['name'] = name
            vlans.append(temp)
print(vlans)

