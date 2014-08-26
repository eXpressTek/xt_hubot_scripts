# Description:
#   Runs a python script that gets a SNMP value from a target host
#
# Dependencies:
#   pysnmp, python and snmp_get.py
#
# Configuration
#   See snmp_get.py for the bulk of the configuration other than moving the conf file to the /conf directory
#
# Commands:
#   snmp
#
# Author:
#   Concept from Stack Overflow (I think) Modified by Daniel Kenner
#

{ spawn } = require 'child_process'

module.exports = (robot) ->
  robot.respond /snmp/i, (msg) ->
    snmp = spawn 'scripts/snmp_get.py'
    msg.send "now running SNMP Quiery. Please wait, may take a minute"
    snmp .stdout.on 'data', ( data ) -> msg.send "#{ data }"
    snmp .stderr.on 'data', ( data ) -> msg.send "There Was an Error: #{ data }"
    #dhcp.on 'close', -> msg.send "DHCP Update Complete"