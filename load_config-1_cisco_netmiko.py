from netmiko import ConnectHandler
from datetime import datetime

cisco_mgmt_ip={
'10.255.255.12',
'10.255.255.22',
#'10.255.255.32'
}


print("Cisco CLI Python = LOAD Config 2")
print("==================================\n")
for ip in cisco_mgmt_ip:
    net_connect = ConnectHandler(
        device_type= "cisco_ios",
        host=ip,
        username="admin",
        password="P@ssw0rd",
    )

    with open('config_file/snmp-c.txt','r') as f:
        config_commands = f.readlines()
        Tstart = datetime.now()
        config_output = net_connect.send_config_set(config_commands)
        print("!!! Configuration has been loaded in "+ip)
        Tend = datetime.now()
        Tdiff = Tend - Tstart
        print("Time taken to push the configuration = " +str(Tdiff)+"\n") 

print("===========End of Program==============")
