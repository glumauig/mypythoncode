from netmiko import ConnectHandler
from datetime import datetime

cisco_iol = {
    'device_type': 'cisco_ios',
    'host': '10.255.255.32',
    'username': 'admin',
    'password': 'P@ssw0rd',
}

net_connect = ConnectHandler(**cisco_iol)
#output = net_connect.send_command('show configuration | display set | no-more')

Tstart = datetime.now()
config_output = net_connect.send_config_from_file('config_file/cr3.txt')
Tend = datetime.now()
print("!!! Configuration has been loaded !!!")
Tdiff = Tend - Tstart
print(config_output)
print("Time taken to push the configuration = " +str(Tdiff)) 
