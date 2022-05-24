#!/usr/bin/python3.9

def get_commands(routerid, name):
    commands = []
    commands.append('hostname ' + name)
    commands.append('router ospf CORE')
    commands.append('router-id ' + routerid)
    return commands

def push_commands(device, commands):
    print('Connecto to device: ' + device)
    for cmd in commands:
        print(cmd)

if __name__== "__main__":
    vpe_file = open('vpe.cfg', 'r')
    vpe_text = vpe_file.read()
    vpe_list = vpe_text.splitlines()
    vpe = []
    for item in vpe_list:
        if 'name' in item:
            temp = {}
            name = item.strip().strip('name').strip()
            temp['name'] = name
            vpe.append(temp)
        elif 'id' in item:
            id = item.strip().strip('id').strip()
            temp['id'] = id
print(vpe)
for node in vpe:
    name = node.get('name')
    rid = node.get('id')
    print('\n')
    print('confugurazione device: ' + name)
    commands = get_commands(rid, name)
    push_commands(name, commands)
    
