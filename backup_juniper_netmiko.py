from netmiko import ConnectHandler

juniper_mx = {
    'device_type': 'juniper_junos',
    'host': '10.255.255.11',
    'username': 'admin',
    'password': 'P@ssw0rd',
}

net_connect = ConnectHandler(**juniper_mx)
output = net_connect.send_command('show configuration | display set | no-more')
#print(output)


filename = f"JR1_config.txt"
with open(filename, 'w') as f:
    f.write(output)


