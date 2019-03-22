conf_file = "NeutronBrain.conf"
def Del_Space(x):
    return x.rstrip(" ").strip(" ")

def Read_Conf(key="ALL"):
    with open(conf_file, "r") as oke:
        oke = oke.read()
        conf = {}
        temp0 = oke.split("\n")
        #remove space and seperate "="    
        temp0 = list(filter(lambda x: not "#" in x, map(lambda x: x.rstrip(" ").strip(" "), temp0))) 
        for i in temp0:
            if (not "=" in i):
                continue
            a = i.split("=")
            conf[Del_Space(a[0])] = Del_Space(a[1])
        if (key=="ALL"):
            return conf
        else:
            try:
                return conf[key]
            except Exception as err:
             print(err)
def Read_Conf_List(key="ALL"):
    return list(map(lambda x: x.replace(" ", ""), Read_Conf(key).split(",")))
