#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime
import sys
from sys import argv

Greeting = sys.argv[1]
Name = sys.argv[2]

print(f'{Greeting} {Name}')
print(datetime.now())

command = subprocess.run(['ls'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print(command)