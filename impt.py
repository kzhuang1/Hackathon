from os import listdir
from os.path import isfile, join
import numpy as np
import lasio

def impt_nm(mypath):
    l = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    li=[x.split('.')[0] for x in l]
    return li

def key_vals(path,keys):
    las_fl = lasio.read(path)
    #vals=[]
    vals = [None] * len(keys)
    iter = 0
    for i in keys:
        vals[iter]=las_fl[i]
        iter=iter+1
    return vals

def mk_lib(mypath,keys):
    names=impt_nm(mypath)
    dnry = {}
    ignr = 0
    for i in names:
        path = mypath+'\\'+i+'.las'
        try:
            dnry[i] = key_vals(path,keys)
        except:
            ignr+=1
            print("ignoring "+i)
            print(ignr)
            
    return dnry

def main():
    #note r is needed to force raw string
    mypath=r"C:\Users\kzhuang\OneDrive\Seisware_Hackathon\code\LAS_notop"
    test = impt_nm(mypath)
    print(test)
    
    las2 = lasio.read(mypath+'\\105622382751170.las')
    t = las2.keys()
    y = las2[t[1]]
   # print(t)
    #print(y)
    test2 = key_vals(mypath+'\\105622382751170.las',t)
        
    keys = ['POR','GR']
    
    x = mk_lib(mypath,keys)    
    
    for key, value in x.items() :
        print (key)
        
    print(x['105622382751170'])
main()


