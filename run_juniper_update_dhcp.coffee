# Description:
#   Runs a python script that updates a DHCP entry in a Juniper
#
# Dependencies:
#   dhcp_update.conf and juniper_update_dhcp.py
#
# Configuration
#   See juniper_update_dhcp.py for the bulk of the work
#
# Commands:
#   dhcp [opts]
#
# Author:
#   Some concepts from file by Sapan Ganguly (Original File) Other concepts from Stack Overflow (I think) 
#   Modified by Daniel Kenner
#

{ spawn } = require 'child_process'

module.exports = (robot) ->
  robot.respond /dhcp (.*)$/i, (msg) ->
    options= msg.match[1]
    opts = []
    #opts.push 'scripts/juniper_update_dhcp.py'
    for opt_val in options.match(/[\w\-\.\:]+/ig)
      opts.push opt_val
    dhcp = spawn 'scripts/juniper_update_dhcp.py',opts
    msg.send "running with options: "+opts
    msg.send "now updating. Please wait, may take a minute"
    dhcp.stdout.on 'data', ( data ) -> msg.send "#{ data }"
    dhcp.stderr.on 'data', ( data ) -> msg.send "There Was an Error: #{ data }"
    #dhcp.on 'close', -> msg.send "DHCP Update Complete"