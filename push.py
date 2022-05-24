#!/usr/bin/env python

#Questa funzione accetta due parametri e appende questi due parametri ad una lista
def get_commands(vlan,name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
    return commands

#Questa funzione scorre una lista con i comandi e stampa i comandi a vide
def push_commands(device, commands):
    print('Connect to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)

#Programma principale
if __name__ == "__main__":
    #Creiamo una lista contenet gli apparati che vogliamo configurare.
    devices =['switch1', 'switch2', 'swotch3']
    #Creiamo un dizionario con l'elenco delle vlan da confiburare.
    vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'}, {'id': '30', 'name': 'WLAN'}]
    
for vlan in vlans:
        vid = vlan.get('id')
        name = vlan.get('name')
        print('\n')
        print('CONFIGURING VLAN: ' + vid)
        commands = get_commands(vid, name)
        for device in devices:
            push_commands(device, commands)
            print('\n')
