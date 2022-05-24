#!/usr/bin/python3.7

if __name__== "__main__":
 COMMANDS = {
   'net': 'net {}',
   'maximum-wait': 'maximum-wait {}',
   'initial-wait': 'initial-wait {}',
   'secondary-wait': 'secondary-wait {}',
 }
 print(COMMANDS)
 CONFIG_PARAMS = {
   'net': '49.cafe.0101.7600.1204.00',
   'maximum-wait': '5000',
   'initial-wait': '1000',
   'secondary-wait': '20'
 }
 command_list = []
 for feature, value in CONFIG_PARAMS.items():
    command = COMMANDS.get(feature).format(value)
    command_list.append(command)
 command_list.insert(0, 'router isis CORE')
 print(command_list)
 print('\n'.join(command_list))
 

