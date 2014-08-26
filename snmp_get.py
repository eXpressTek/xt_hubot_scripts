#!/usr/bin/python
import os, sys
import socket
import random
from struct import pack, unpack
from datetime import datetime as dt

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import Integer, IpAddress, OctetString
import ConfigParser

def do_snmp_get(
  ip='REDACTED',
  community='REDACTED',
  value=(1,3,6,1,4,1,2636,3,1,13,1,7,9,1,0,0)):

  generator = cmdgen.CommandGenerator()
  comm_data = cmdgen.CommunityData('server', community, 1) # 1 means version SNMP v2c
  transport = cmdgen.UdpTransportTarget((ip, 161))

  real_fun = getattr(generator, 'getCmd')
  res = (errorIndication, errorStatus, errorIndex, varBinds)\
      = real_fun(comm_data, transport, value)

  if not errorIndication is None  or errorStatus is True:
         print 'Error: %s %s %s %s' % res
  else:
    return varBinds
#    for key, val in varBinds:
#         print '{0}={1}'.format(key,val)
         

         
if __name__ == '__main__':
#  print do_snmp_get(ip='172.16.16.1',community='<redacted>',value=(1,3,6,1,4,1,2636,3,1,13,1,7,9,1,0,0))
  config = ConfigParser.RawConfigParser()
  config.read('/conf/snmp_get.conf')
  
  try:
    comm = config.get("Configuration", "community")
    host = config.get("Configuration", "host")
  except ConfigParser.NoOptionError:
      print "Community and Host variables are not set in config file. Please see Systems Operator for Hubot"
  try:
    value = config.get("Configuration", "value")
    sys.exit(1)
  except ConfigParser.NoOptionError:
      print "Assuming Default SNMP Value"
  print do_snmp_get(community=comm, ip=host)