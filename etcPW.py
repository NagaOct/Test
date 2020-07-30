mport json

def read():
    text = open("/etc/passwd").read()
    return text
            
s1 = read().split("\n")
for i in range(len(s1)):
    if s1[i] == "":
        break
    s2 = s1[i].split(":")
    list = [("user",s2[0]),("pass",s2[1]),("uid",s2[2]),("gid",s2[3]),("description",s2[4]),("home",s2[5]),("shell",s2[6])]
    mydict = dict(list)
    s1[i] = mydict

print json.dumps(s1,indent = 4)

