import json
from collections import OrderedDict

def read():
    #text = open("/etc/passwd").read()
    text = open("dummy.txt").read()
    return text
            
s1 = read().split("\n")
mydict = OrderedDict()
for i in range(len(s1)):
    if s1[i] == "":
        break
    s2 = s1[i].split(":")
    mydict["user"] = s2[0]
    mydict["pass"] = s2[1]
    mydict["uid"] = s2[2]
    mydict["gid"] = s2[3]
    mydict["description"] =s2[4]
    mydict["home"] = s2[5]
    mydict["shell"] =s2[6]

    s1[i] = mydict.copy()

print json.dumps(s1,indent = 4)

