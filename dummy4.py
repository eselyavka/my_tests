#!/usr/bin/env python2.7

def printer():
    print reduce(lambda x,y: x*y, [x for x in range(1,10)])

if __name__ == '__main__':
    printer()
