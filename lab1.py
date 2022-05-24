#!/usr/bin/env python3.9

if __name__ == "__main__":
 hosts_file = open('hosts', 'r')
 hosts_text = hosts_file.read()
 hosts_list = hosts_text.splitlines()

 for i in hosts_list:
     if i[0].isdigit:
      print(i)
     else:
      print("non è un numero")

