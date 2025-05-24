#!/usr/bin/env python3

# Author: Robby Geanrebb Agabon
# Author ID: rgagabon@myseneca.ca
# Date Created: 2025-05-18

import sys

if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0])
    sys.exit(1)

timer = int(sys.argv[1])
            

while timer > 0:
    print(str(timer))
    timer = timer - 1
print('blast off!')