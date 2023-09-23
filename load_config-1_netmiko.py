from netmiko import ConnectHandler
from datetime import datetime

juniper_mgmt_ip={
'10.255.255.11',
'10.255.255.21',
'10.255.255.31'
}


print("Juniper CLI Python = LOAD Config 2")
print("==================================\n")
for ip in juniper_mgmt_ip:
    net_connect = ConnectHandler(
        device_type= "juniper_junos",
        host=ip,
        username="admin",
        password="P@ssw0rd",
    )

    with open('config_file/snmp-j.txt','r') as f:
        config_commands = f.readlines()
        Tstart = datetime.now()
        config_output = net_connect.send_config_set(config_commands, exit_config_mode=False)
        Tend = datetime.now()
        print("!!! Configuration has been loaded in "+ip)
        print("Commiting now ... ")
        config_output = net_connect.commit()
        Tdiff = Tend - Tstart
        print(config_output)
        print("Time taken to push the configuration = " +str(Tdiff)+"\n") 

print("===========End of Program==============")
