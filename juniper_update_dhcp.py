#!/usr/bin/python
from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys, getopt
import ConfigParser

#make a timestamp
def stamp():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ ",time.gmtime())

debug = False

def main(argv):
    config = ConfigParser.RawConfigParser()
    config.read('/conf/juniper_update_dhcp.conf')
    username = ""
    password = ""
    host = ""
    try:
        username = config.get("Configuration", "user")
        password = config.get("Configuration", "password")
        host = config.get("Configuration", "host")
    except ConfigParser.NoSectionError:
        print "Username, Password, Or Host not set in Configuration File, If not set in options, the script will fail"
    mac = ''
    ipAddr = ''
    hostname = ''
    try:
       opts, args = getopt.getopt(argv,"u:p:h:m:i:H:",["user=","pass=","host=","mac=","ip=","hostname=","help",])
    except getopt.GetoptError:
       print 'juniper_update_dhcp -u/--user <username> -p/--pass <password> -h/--host <juniper ip/hostname> -m/--mac <MAC Address> -i/--ip <IP Address Reservation> -H/--hostname <Hostname Reservation> --help (shows this message)'
       sys.exit(2)
    for opt, arg in opts:
        if opt == '--help':
            print 'juniper_update_dhcp -u/--user <username> -p/--pass <password> -h/--host <juniper ip/hostname> -m/--mac <MAC Address> -i/--ip <IP Address Reservation> -H/--hostname <Hostname Reservation> --help (shows this message)'
            sys.exit()
        elif opt in ("-u", "--user"):
            username = arg
        elif opt in ("-p", "--pass"):
            password = arg
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-m", "--mac"):
            mac = arg
        elif opt in ("-i", "--ip"):
            ipAddr = arg
        elif opt in ("-H", "--hostname"):
            hostname = arg
    if (username == "") or (password == "") or (host == "") or (mac == "") or (ipAddr == "") or (hostname == ""):
        print 'juniper_update_dhcp -u/--user <username> -p/--pass <password> -h/--host <juniper ip/hostname> -m/--mac <MAC Address> -i/--ip <IP Address Reservation> -H/--hostname <Hostname Reservation> --help (shows this message)'
        sys.exit()
    if debug:
        print "username: "+username+", password: "+password+", host: "+host+", MAC: "+mac+", IP Address: "+ipAddr+", hostname: "+hostname
    
    
    
    dev = Device(host=host, user=username, password=password, port='22' )

    dev.open()
    
    cu = Config(dev)

    confVars = {}
    confVars['MAC_ADDR'] = mac
    confVars['IP_ADDR'] = ipAddr
    confVars['HOSTNAME'] = hostname
    
    cu.load(template_path='dhcp_update.conf', template_vars=confVars)

    cu.commit()

    #pprint( dev.facts )

    dev.close()
    
    print "Appears to have updated successfully."

if __name__ == "__main__":
   main(sys.argv[1:])


