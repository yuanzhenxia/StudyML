#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re


def isValid(arg):
    match = re.match('[aeiouàáâèéêìíîóòôúùû][135][bcdefghjklmnpqrstvwxyz][aeiouàáâèéêìíîóòôúùû]',arg,re.I)
    if match and len(arg.strip())==4:
        return True;
    else:
        return False;

def wt(arg):
    fn = open("/Users/lance/Codes/nl.txt","w+")
    fn.writelines(arg)
    fn.close()
    return;




st = ""
smap = {}
with open("/Users/lance/Codes/hyph-nl.tex","r+") as f:
    for line in f.readlines():
        if isValid(line):
            print line
            k = line[0]+line[3]
            if k in smap.keys():
                v = smap.get(k)
                v.append(line[2])
            else:
                v = []
                v.append(line[2])
                smap[k]=v

stks = sorted(smap.keys())
for k1 in stks:
    zj = ""
    for v1 in smap.get(k1):
        zj=zj+v1
    st = st +k1[0]+" ["+zj+"] "+k1[1]+"\n"
    
print st
#wt(st)

def isYuan(arg):
    if arg=='a' or arg=='e' or arg=='i' or arg=='o' or arg=='u':
        return True;
    else:
        return False;
    
    

    


    
