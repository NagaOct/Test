import json

def read():
    text = open("/etc/passwd").read()
    return text

s1 = read().split("\n")

# t = raw_input()
for i in s1:
    print json.dumps(i.split(":"), indent = 4)
