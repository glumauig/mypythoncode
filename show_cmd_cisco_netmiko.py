#!/usr/bin/python3
from netmiko import ConnectHandler

cisco_iol = {
    'device_type': 'cisco_ios',
    'host': '10.255.255.12',
    'username': 'admin',
    'password': 'P@ssw0rd',
    #'ssh_config_file': '~/.ssh/cisco_iol_config',
}

net_connect = ConnectHandler(**cisco_iol)
output = net_connect.send_command('show run')
print(output)
