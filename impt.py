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
        print(las_fl[i])
        vals[iter]=las_fl[i]
        iter=iter+1
    return vals

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
    
    
    
    
    keys = ['POR','GR','RHOB']
    
    
    
    
main()
