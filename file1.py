y=open("running-config.cfg","r")
def list_ifname_ip(y):
    ip_dic={}  
    for line in y:
        if 'no' not in line:
            if 'nameif' in line:
                line=line.strip()
                key=line.split(" ")
            if 'ip address' in line and '.' in line:
                line=line.strip()
                iptemp=line.split(" ")
                tup=(iptemp[2],)
                ip_dic.setdefault(key[1],(iptemp[2],iptemp[3]))
           
    return ip_dic

print(list_ifname_ip(y))

