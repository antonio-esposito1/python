from __future__ import print_function
import sys
import libvirt
conn = libvirt.open('qemu+ssh://antonio@192.168.1.8/system')
if conn == None:
 print('Failed to opne', file=sys.stderr)
 exit(1)
 print('Connection Successfull')
 conn.close()
 print('Conn Closed')
 exit(0)

