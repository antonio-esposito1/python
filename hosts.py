#!/usr/bin/python3.7

if __name__== "__main__":
 import yaml
 config = open('device.cfg', 'w')
 with open("hosts-mgmt.yml") as f:
  devices = yaml.load(f)
  print(devices)
  type(devices)
  for key, value in devices.items():
   if 'mivpe013' in value:
    print('telnet ' + value)
    config.write('telnet ' + value + '\n')
    config.write('router isis CORE')
    #config.write('net' + value2)

config.close()


