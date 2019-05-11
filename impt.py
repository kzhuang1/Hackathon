from os import listdir
from os.path import isfile, join

def impt(mypath):
    l = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    li=[x.split('.')[0] for x in l]
    return li

"""
def main():
    #note r is needed to force raw string
    mypath=r"C:\Users\kzhuang\OneDrive\Seisware_Hackathon\code\LAS"
    test = impt(mypath)
    print(test)
    
main()
"""