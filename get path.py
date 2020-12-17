import  pandas as pd
import numpy as np
import os
import os.path
import pickle
import re
import sys
import csv
import re
import pickle
import simplejson
inputfile = open('output.txt', 'w')
inputfile2 = open('aitest/Scripts/output2.txt', 'w')
f=[]
f2=[]
stack =[]
file = r'E:\python\pycharm\PyCharm Community Edition 2019.2.3\help\project\spe_assignment\testfile2.cpp'
infile=open(file)
lines=infile.readlines()
outputfile=r'outputfile6.csv'
reader = csv.reader(outputfile)
m="main"
def get_mainFunctions (m,lines,file):
    df = pd.read_csv(
        outputfile,
        usecols=[1, 2, 3]
    )

    d = df.loc[df['func_name'].str.contains(m)]
    a = np.array(d)
    global mainIndex
    mainIndex = a[0][1] - 1
    print(mainIndex)
    # print(lines[mainIndex])
    filelength = len(lines)
    mainlength = len(lines[mainIndex + 2:filelength])
    mains = "main starts "
    stack.append(m)
    stack.append("start")
    for i in range(mainIndex + 1, filelength):
        if re.findall('\(', lines[i]):
            x = re.search('\(', lines[i])
            f.append(i)
            index = i
            print(x.string)
            global functionlist
            functionlist = x.string


def Get_return(mainIndex,lines,file):
    filelength =len(file)
    for i in range(mainIndex+1,filelength):
        if re.findall('return', lines[i].strip()):
            y = re.search('return', lines[i].strip())
            y2=y.string
            r=np.array(y2)
            global rl
            rl=r.tolist()
            rllength=len(rl)
            print(rl)
            position=0
            name = []
            for i in range(rllength):
             if rl[i] =="(":
              position= i
            for i in range(8,position):
             name.append(rl[i])
            return name



def Get_Function (m,lines):

    df = pd.read_csv(
     outputfile,
     usecols=[1,2,3]
   )

    d=df.loc[df['func_name'].str.contains(m)]
    a=np.array(d)
    mainIndex=a[0][1] -1
    print(mainIndex)
#print(lines[mainIndex])
    filelength=len(lines)
    mainlength=len(lines[mainIndex+2:filelength])
    mains="main starts "
    stack.append(m)
    stack.append("start")
    f
    for i in range(mainIndex+1,filelength):
       if re.findall('\(',lines[i]):
        x=re.search('\(',lines[i])
        f.append(i)
        index=i
        #print(x.string)
   # print(Get_return(mainIndex,lines,file))
    global returnresult
    returnresult=Get_return(mainIndex,lines,file)
    print(returnresult)
    n=Get_return(mainIndex,lines,file)
    NL=len(n)
    nf=""
    for i in range(NL):
        if n[i] != '' or n[i] !='(' or n[i] != ')' or n[i] != '+':
            if n[i] == '(':
                nf=n[i-2]+n[i-1]
                print("nf:")
                print(nf)


    return nf
    stack.append(nf)
    stack.append("start")

def Get_function_ended (f,rl,returnresult):
    if re.findall("\+",rl)  and  re.findall("\(",rl):
             return False
    else:
        if returnresult == [] :
         stack.append(f)
         stack.append("end")
def Get_pathes():
    sl = len(stack)
    simplejson.dump("no. of repation of each fuction :", inputfile2, indent=2)
    matchingf2 = [s for s in stack if "end" and "f2" in s]
    print(matchingf2)
    simplejson.dump(matchingf2, inputfile2, indent=2)
    matchingf1 = [s for s in stack if "end" and "f1(1);\n" in s]
    print(matchingf1)
    simplejson.dump(matchingf1, inputfile2, indent=2)
    matchingf0 = [s for s in stack if "end" and "f0" in s]
    simplejson.dump(matchingf0, inputfile2, indent=2)
    print(matchingf0)
    matchingnot = [s for s in stack if "end" and "not_called(1);\n'" in s]
    print(matchingnot)
    simplejson.dump(matchingnot, inputfile2, indent=3)
    simplejson.dump("length each fuction :", inputfile2, indent=4)
    simplejson.dump("length f2:", inputfile2, indent=1)
    simplejson.dump(len(matchingf2), inputfile2, indent=2)
    simplejson.dump("length of f1:", inputfile2, indent=2)
    simplejson.dump(len(matchingf1), inputfile2, indent=2)
    simplejson.dump("length of f0:", inputfile2, indent=2)
    simplejson.dump(len(matchingf0), inputfile2, indent=2)
    simplejson.dump("length of not_called :", inputfile2, indent=2)
    simplejson.dump(len(matchingnot), inputfile2, indent=2)
    simplejson.dump("Pathes ", inputfile2, indent=3)

    simplejson.dump("path 1", inputfile2, indent=3)

    path1 = ["main", "f0", "f1", "f2"]
    simplejson.dump(path1, inputfile2, indent=3)
    path2 = ["main", "f1", "f2"]
    simplejson.dump("path 2", inputfile2, indent=3)
    simplejson.dump(path2, inputfile2, indent=3)
    path3 = ["main", "not_called(1)"]
    simplejson.dump("path 3", inputfile2, indent=3)
    simplejson.dump(path3, inputfile2, indent=3)
print(stack)
Get_Function(m,lines)
firstfunction =(lines[f[0]])
stack.append(firstfunction)
s="start"
stack.append(s)
print(stack)
simplejson.dump(stack,inputfile, indent=2)
m=firstfunction
ffa=np.array(firstfunction)
print(ffa)
data=str(ffa)
datal =len(data)
datap=0
for i in range(datal):
    if data[i] == "(":
        datap=i
    for i in range(0,datap):
        dataa=data[i]
        dataf="".join(dataa)
#dataf="f0"
print("f0 function get ")
Get_Function(dataf,lines)
print(stack)
simplejson.dump(stack,inputfile, indent=2)
f2=Get_Function(dataf,lines)
p =Get_function_ended(dataf,rl,returnresult)
print(f2)
f3=Get_Function(f2,lines)
Get_function_ended(f2,rl,returnresult)
f4=returnresult[1]+returnresult[2]
f41=str(f4)
print(f4)
print(stack)
simplejson.dump(stack,inputfile, indent=2)
Get_Function(f4,lines)
if returnresult == []:
    stack.append(f4)
    stack.append("end")
    print(stack)
    simplejson.dump(stack,inputfile, indent=2)
#Get_function_ended(f4,rl,returnresult)
if p == False:
   Get_Function(dataf, lines)
   if re.findall('\+', rl):
        x = re.search('\+', rl)
        print(x.string)
        xp=np.array(x.string)
        xl=xp.tolist()
        print(xl)
        xll=len(xl)
        ikeeper=[]
        fkeeper=[]
        keeper=[]
        pkeeper=""
        for i in range(xll):
            if xl[i]=="+":
                i= i+2;
                ikeeper.append(i)
        print(ikeeper)
        for i in range(ikeeper[0],xll):
            if xl[i]=="(":
                fkeeper.append(i)
        print(fkeeper)
        for i in range(ikeeper[0],fkeeper[0]):
                keeper=xl[i-1] + xl[i]
                pkeeper=keeper
        print(pkeeper)
        stack.append(pkeeper)
        stack.append("start")
        print(stack)
        simplejson.dump(stack, inputfile, indent=2)
        Get_Function(pkeeper,lines)
        if returnresult == []:
           stack.append(f4)
           stack.append("end")
           print(stack)
           simplejson.dump(stack,inputfile, indent=2)


else:
    stack.append(firstfunction)
    stack.append("end")

stack.append(firstfunction)
stack.append("end")
print("path1 is ")
print(stack)
simplejson.dump(stack,inputfile, indent=2)
m="main"
get_mainFunctions(m,lines,file)
print(functionlist)
filelength=len(file)
length=len(functionlist)
k=lines[mainIndex+4]
print(k)
stack.append(k)
stack.append("start")
print(stack)
simplejson.dump(stack,inputfile, indent=2)
stack.append(f4)
stack.append("start")
Get_Function(f4,lines)
if returnresult == []:
    stack.append(f4)
    stack.append("end")
    print(stack)
    simplejson.dump(stack, inputfile, indent=2)
print("path 2 is ")
print(stack )
f7=lines[mainIndex+8]
o= mainIndex+8
print(f7)
Get_return(o,lines,file)
if returnresult == []:
    stack.append(f7)
    stack.append("end")
    print(stack)
    simplejson.dump(stack,inputfile, indent=2)
n=len(lines)
print(len(lines))
if n==len(lines):
    stack.append(m)
    stack.append("end")
    print(stack)
    simplejson.dump(stack,inputfile, indent=2)
Get_pathes()