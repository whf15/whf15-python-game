#!/usr/bin/env python
# coding: utf-8

# In[41]:


import sys
import os
import time
import _thread
import datetime
import platform
import socket

def get_os():
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"
    
def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),"1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()
    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >=0:
            flag = True
            break
    if flag:
        print("*** *** *** ip: %s is OK *** *** ***"%(ip_str))
        print("ip hostname : %s"%(socket.getfqdn(ip_str)))
def find_ip(ip_prefix):
    for i in range(1,256):
        ip = ('%s.%s'%(ip_prefix,i))
        _thread.start_new_thread(ping_ip,(ip,))
        time.sleep(0.5)
        
if __name__ == "__main__":
    startTime = datetime.datetime.now()
    print("start time %s"%(time.ctime()))
    net=sys.argv[1]
    args = "".join(("192.168."+net+".1"))
    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
    endTime = datetime.datetime.now()
    print("end time %s"%(time.ctime()))
    print("total takes :",(endTime - startTime).seconds)


# In[38]:


# import socket
# import uuid

# # 获取主机名
# hostname = socket.gethostname()
# #获取IP
# ip = socket.gethostbyname(hostname)
# # 获取Mac地址
# def get_mac_address():
#     mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
#     return ":".join([mac[e:e+2] for e in range(0,11,2)])

# # ipList = socket.gethostbyname_ex(hostname)
# # print(ipList)
# print("主机名：",hostname)
# print("IP：",ip)
# print("Mac地址：",get_mac_address())


# In[40]:


# socket.getfqdn('192.168.229.1')


# In[ ]:




