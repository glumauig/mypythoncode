from netmiko import ConnectHandler
from datetime import datetime

juniper_mx = {
    'device_type': 'juniper_junos',
    'host': '10.255.255.21',
    'username': 'admin',
    'password': 'P@ssw0rd',
}

net_connect = ConnectHandler(**juniper_mx)
#output = net_connect.send_command('show configuration | display set | no-more')

with open('config_file/jr2.txt','r') as f:
    config_commands = f.readlines()
    Tstart = datetime.now()
    config_output = net_connect.send_config_set(config_commands, exit_config_mode=False)
    Tend = datetime.now()
    print("!!! Configuration has been loaded !!!")
    print("Commiting now ... ")
    config_output = net_connect.commit()
    Tdiff = Tend - Tstart
    print(config_output)
    print("Time taken to push the configuration = " +str(Tdiff)) 
