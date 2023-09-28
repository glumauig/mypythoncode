#!/usr/bin/python3
#!/usr/local/bin/python3
from netmiko import ConnectHandler
from datetime import datetime

juniper_ip={
'10.255.255.11',
'10.255.255.21'
}

for ip in juniper_ip:
    net_connect = ConnectHandler(
            device_type="juniper_junos",
            host=ip,
            username="admin",
            password="P@ssw0rd",
    )
    output = net_connect.send_command('show configuration | display set | no-more')
    datetoday = datetime.now()
    datetoday = datetoday.strftime("%m-%d-%Y_%H%M%S")
    filename = f"/home/u-admin/pythoncode/backup_folder/"+datetoday+"-"+ip+".conf"
    with open(filename, 'w') as f:
        f.write(output)
