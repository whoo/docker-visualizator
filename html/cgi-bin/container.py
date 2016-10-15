#!/usr/bin/env python

from docker import Client
import json

cli=Client()

def GetInfo(cli):
    data=[]
    base="/sys/fs/cgroup/memory/docker"
    for k,el in enumerate(cli.containers()):
        info={}
        info['Names']=el['Names'][0]
        info['Command']=el['Command']
        ram=int(open(base+"/"+el['Id']+"/memory.usage_in_bytes","r").read()[:-1])
        info['mem']=ram
        mram=int(open(base+"/"+el['Id']+"/memory.max_usage_in_bytes","r").read()[:-1])
        info['memmax']=mram
        data.append(info)


    return json.dumps(data)




print("Content-type: application/json")
print("");
print (GetInfo(cli))
