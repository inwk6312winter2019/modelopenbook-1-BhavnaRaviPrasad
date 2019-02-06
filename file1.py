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

def replace_str():
    myfile = open("running-config.cfg","r")
    newfile = open("new-running-config.cfg","w")
    for my in myfile:
        mylist = my.split()
        if "255.255.0.0" in my:
            line = my.replace("255.255.0.0","255.0.0.0")
            newfile.write(line)
        elif "255.255.255.0" in my:
            line  = my.replace("255.255.255.0","255.0.0.0")
            newfile.write(line)
        elif "172" in my:
            line = my.replace("172","10")
            newfile.write(line)
        elif "192" in my:
            line = my.replace("192","10")
            newfile.write(line)
        else:
            newfile.write(my)
print(replace_str())

def create_list():
    myfile = open("running-config.cfg","r")
    transit_access_in = []
    fw_management_access_in = []
    global_access = []
    for my in myfile:
        if "transit_access_in" in my:
            my = my.strip()
            transit_access_in.append(my)
        if "fw-management_access_in" in my:
            my = my.strip()
            fw_management_access_in.append(my)
        if "global_access" in my:
            my = my.strip()
            global_access.append(my)

    print("\ntransit_access list:",transit_access_in)
    print("\nfw_management_list:",fw_management_access_in)
    print("\nglobal_access list:",global_access)

create_list()
