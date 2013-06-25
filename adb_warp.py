#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys,os
import subprocess
import time

PATH_TO_ADB = "adb"

def execcmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()

def main() :
    if(len(sys.argv) <= 1) :
        print "usage:  adb_warp.py cmd..."
        return
    cmd = PATH_TO_ADB
    for each in sys.argv[1:] :
        cmd += " " + each
    out,err = execcmd(cmd)

    if(not err.startswith("error:")) :
        print out
        return
    else :
        cmd = PATH_TO_ADB + " devices"
        out,err = execcmd(cmd)
        print out
        deviceList = out.split('\n')
        num = raw_input("select a device to exectue command:")
        num = int(num)
        if (num>(len(deviceList)-3)) :
            print "wrong number"
            return 
        deviceName = deviceList[num].strip().split()[0]
        cmd = PATH_TO_ADB + " -s " + deviceName
        for each in sys.argv[1:] :
            cmd += " " + each
        out,err = execcmd(cmd)
        print out

if __name__ == '__main__' :
    main()
