import os


"""ip_list = ("192.168.0.101", "192.168.0.102", "192.168.0.103", "192.168.0.104", "192.168.0.105",
           "192.168.0.106", "192.168.0.107", "192.168.0.108", "192.168.0.9", "192.168.0.10",
           "192.168.0.111", "192.168.0.112", "192.168.0.113", "192.168.0.114", "192.168.0.115",
           "192.168.0.116", "192.168.0.117", "192.168.0.118", "192.168.0.119", "192.168.0.120",
           "192.168.0.121", "192.168.0.122", "192.168.0.123", "192.168.0.124","192.168.0.125",)"""
ip_list = ("192.168.0.125",
           "192.168.0.126")
os.system("clear")
for x in range(4): print "************************************************"
ip_status_list = []

for ip in ip_list:
# hostname = "google.com"
    response = os.system("ping -t 10 " + ip)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    ip_status_list.append("IP %s condition is %s"%(ip, pingstatus))
for status in ip_status_list:
    print status


#hostname = "192.168.100.73"
#response = os.system("ping -c 1 " + hostname)
