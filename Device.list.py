#!/usr/bin/python3.9
def print_list_and_lenght(list_device_par):
   print(list_device_par)
   print(len(list_device_par))

if __name__== "__main__":
 import yaml
 config = open('device.cfg', 'w')
 with open("hosts-mgmt.yml") as f:
  devices = yaml.load(f)
  print(devices)
  type(devices)
  device_list =[]
  device_dictinary = {}
  for key, value in devices.items():
   device_list.append(value)
   print(key + ': ' + value)
   if 'mivpe013' in value:
    print('telnet ' + value)
    config.write('telnet ' + value + '\n')
    config.write('router isis CORE')
  print_list_and_lenght(device_list)
  device_list.pop()
  print(device_list)
  print_list_and_lenght(device_list)
  device_list.pop(device_list.index('fedora31'))
  print_list_and_lenght(device_list)
  device_list.sort()
  print(device_list)
  print(devices['10.176.1.27'])
  print(devices.get('10.176.1.208', False))
  print(devices)
  print(devices.values())
  print(devices.keys())
  print(devices.pop('10.176.1.28'))
  print(devices)
config.close()

