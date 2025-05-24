#!/usr/bin/env python3


import sys

# Checking for correct number of arguments
if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit(0)

name = sys.argv[1]
age = int(sys.argv[2])

print ('Hi ' + name + ', you are ' + str(age) + ' years old.')