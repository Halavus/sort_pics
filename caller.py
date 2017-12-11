#!/usr/bin/python

from subprocess import Popen as Popen
from subprocess import PIPE as PIPE

def caller(lst): 
    '''bash command if more than 1 word have to be in a list'''
    proc = Popen(lst, stdout=PIPE)
    output = proc.stdout.read()
    return output
