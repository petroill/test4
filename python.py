#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

print("Hello World")
print(datetime.now())

command = subprocess.run(['ls'], stdout=subprocess.PIPE).stdout.decode('utf-8')
print(command)