#!/usr/bin/env python

from docker import Client
import json

cli=Client()

def GetImageTree(cli):
    node=cli.images(quiet=True,all=True)
    edgesArray=[]

    for v,a in enumerate(cli.images(all=True)):
        try:
    #        print("%s,%s"%(v,node.index(a['ParentId'])))
            edgesArray.append({'from':v,'to':node.index(a['ParentId']) })
        except:
            pass

    nodesArray=[]
    for v,a in enumerate(cli.images(all=True)):
        group=0;
        name="<none>:<none>"
        try:
            name=a['RepoTags'][0]
        except:
            name="<none>:<none>"

        if (a['ParentId']==""):
            group=4;

        if (name=="<none>:<none>"):
            group=2;
        nodesArray.append( {'id':v, 'label':name, 'group': group} )

    data={'nodes':nodesArray,'edges':edgesArray}
    return json.dumps(data)
    #return (data);


print("Content-type: application/json")
print("");
print(GetImageTree(cli))
