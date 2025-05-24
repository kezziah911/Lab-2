#!/usr/bin/env python3

# Author: Robby Geanrebb Agabon
# Author ID: rgagabon@myseneca.ca
# Date Created: 2025-05-18

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3
    
            

while timer > 0:
    print(str(timer))
    timer = timer - 1
print('blast off!')