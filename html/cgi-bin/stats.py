#!/usr/bin/env python

from docker import Client
import json

cli=Client()

def GetInfo(cli):
    data={}
    base="/sys/fs/cgroup/memory/docker"
    cur=open(base+"/memory.usage_in_bytes","r").read()[:-1]
    data["current"]=int(cur)
    max=open(base+"/memory.max_usage_in_bytes","r").read()[:-1]
    data["max"]=int(max)-int(cur)

    data["max memmory"]=int(cli.info()["MemTotal"])-int(max)

    return json.dumps(data)




print("Content-type: application/json")
print("");
print (GetInfo(cli))
