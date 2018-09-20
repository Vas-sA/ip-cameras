
# coding: utf-8

# In[1]:


import subprocess


# In[2]:


def extract_ip_from_file(fileName):
    ip = []
    with open(fileName, 'r') as file:
        for line in file.readlines():
            line = line.rstrip()
            if '-' in line:
                tmp = ip_range(line)
                for i in tmp:
                    ip.append(i)
            else:
                ip.append(line)
    
    return ip


# In[3]:


def decode_bytes_list(batesList):
    strings = []
    for i in batesList:
        strings.append(i.decode('UTF-8'))
    
    return strings


# In[4]:


def ip_range(string):
    
    start_ip, end_ip = string.split('-')   
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))    
    ip_range = []
    
    
    for i in range(4):
        if start[i] > end[i]:
            tmp = start
            start =  end
            end = tmp
            start_ip = end_ip
            break
            
    temp = start   
    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
        ip_range.append(".".join(map(str, temp)))    
      
    return ip_range
   


# In[5]:


def detect_host(ip):
    params = ['nmap','-sP', ip]
    res = decode_bytes_list(subprocess.check_output(params).splitlines())
    
    return res


# In[6]:


# if you know that here there is camera on this ip
#but it should be useless method for secured cameras
#def deepest_scan_ip(ip):
#    params = ['nmap','-p-','-A', ip]
#    res = decode_bytes_list(subprocess.check_output(params).splitlines())
#    pprint.pprint(res)
#    return res  


# In[25]:


def get_up_hosts(ip_list):
    up = []
    for ip in ip_list:
        tmp = detect_host(ip)
        if len(tmp) == 5:
            up.append(ip)
        else:
            pass
            
            
    return up


# In[59]:


def check_if_cam(ip):
    params = ['nmap','-A', ip]
    res = decode_bytes_list(subprocess.check_output(params).splitlines())
    testLine = '.'.join(res[-5:-2])
    if 'webcam' in testLine:
        
        print(ip)
        with open('cameras.txt', 'a') as file:
            for line in res:
                file.write(line+'\n')
    return res





# In[49]:


def main():
    print('  check cameras.txt for more details after scan  \n cameras: ')
    for i in get_up_hosts(extract_ip_from_file('input.txt')):
        check_if_cam(i)
   


# In[43]:


if __name__ == "__main__":
    # execute only if run as a script
    main()

