#!/usr/bin/python
import os
from openstack import connection
from prettytable import PrettyTable

auth_args = {
    'auth_url': os.environ['OS_AUTH_URL'],
    'project_name': os.environ['OS_PROJECT_NAME'],
    'username': os.environ['OS_USERNAME'],
    'password': os.environ['OS_PASSWORD'],
    'user_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
    'project_domain_name': os.environ['OS_PROJECT_DOMAIN_NAME'],
}

cpu_allocation_ratio = 1.5
disk_allocation_ratio = 1.0
ram_allocation_ratio = 1.0

color_tbl = {
"grey": '\033[1;30m',
"green" :'\033[32m',
"blue" : '\033[34m',
"yellow" :'\033[33m',
"red" : '\033[31m',
}
def colorizer(num):
    if num <= 20:
        return "%s%.2f%%\033[0m" % (color_tbl['grey'], num)
    if num <= 40:
        return "%s%.2f%%\033[0m" % (color_tbl['green'], num)
    if num <= 60:
        return "%s%.2f%%\033[0m" % (color_tbl['blue'], num)
    if num <= 80:
        return "%s%.2f%%\033[0m" % (color_tbl['yellow'], num)
    return "%s%.2f%%\033[0m" % (color_tbl['red'], num)

conn = connection.Connection(**auth_args)
tbl = PrettyTable(["hostname", "ip", "status", "state", "cpu", "cpu_ratio", "ram", "ram_ratio", "disk", "disk_ratio"])
tbl.align['hostname'] = 'l'
tbl.align['ip'] = 'l'
#tbl.padding_width = 2

for i in conn.compute.hypervisors():
     host = conn.compute.get_hypervisor(i.id)
     cpu = str(host.vcpus_used) + "/" + str(host.vcpus)
     cpu_ratio = colorizer(host.vcpus_used * 100.0 / (host.vcpus * cpu_allocation_ratio))
     ram = str(host.memory_used) + "/" + str(host.memory_size)
     ram_ratio = colorizer(host.memory_used * 100.0 / (host.memory_size * ram_allocation_ratio))
     disk = str(host.local_disk_used) + "/" + str(host.local_disk_size)
     disk_ratio = colorizer(host.local_disk_used * 100.0 / (host.local_disk_size * disk_allocation_ratio))
     status = host.status
     status = "%s%s\033[0m" % (color_tbl['red'], status) if status != "enabled" else status
     state = host.state
     state =  "%s%s\033[0m" % (color_tbl['red'], state) if state != "up" else state
     
     tbl.add_row([host.name, host.host_ip, status, state,
                  cpu, cpu_ratio,
                  ram, ram_ratio,
                  disk, disk_ratio])
print tbl

