#Not used, not debbugged, not ran even once
#Use on your own risk, beware errors

import idaapi
import idautils
import idc
base = 0x10000
def do_rename(l):
    splitted = l.split()
    straddr = splitted[0]
    strname = splitted[1].replace("\r", "").replace("\n", "")
    if straddr.find(":") != -1: #assuming form segment:offset
        #removing segment, offset should be unique, if it isn't so, we should handle it differently
        straddr = straddr.split(":")[1]
    #idc.MakeCode(eaaddr)
    #idc.MakeFunction(eaaddr)
    idc.MakeName(base+int(straddr, 16), strname )


if __name__ == "__main__":
    f = open( "a8.txt", "r")
    #idc.MakeName(66960, "ars" )
    for l in f:
        do_rename(l)
    f.close()
