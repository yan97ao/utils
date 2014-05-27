#!/usr/bin/python2
# -*- coding: utf-8 -*-

from graphviz import Digraph    #pip install graphviz
import sys
import os

def dirwalk(path):
    print path
    for i in os.listdir(path):
        fullpath = os.path.join(path,i)
        print fullpath
        if os.path.isdir(fullpath):
            dirwalk(fullpath)

def main() :
    if(len(sys.argv) != 2) :
        print "usage:  dir2pic.py PATH"
        return
    path = sys.argv[1]
    dirwalk(path)

if __name__ == '__main__' :
    main()
