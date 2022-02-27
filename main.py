import sys


def count(a,b):
    return a+b

def customPrint(a):
    sys.stdout.write(str(a))


customPrint(count(1,2))