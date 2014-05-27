#!/usr/bin/python2
# -*- coding: utf-8 -*-

from graphviz import Digraph    #pip install graphviz
import sys
import os

def dirwalk(dot,path):
    print path
    for i in os.listdir(path):
        if i.startswith('.'):
            continue

        fullpath = os.path.join(path,i)
        dot.node(fullpath,i)
        dot.edge(os.path.dirname(fullpath),fullpath)
        if os.path.isdir(fullpath):
            dirwalk(dot,fullpath)

def main() :
    if(len(sys.argv) != 2) :
        print "usage:  dir2pic.py PATH"
        return

    dot = Digraph()

    path = sys.argv[1]
    dirwalk(dot,path)
    dot.render("out.gv")
    
if __name__ == '__main__' :
    main()
