import time 
import subprocess
from subprocess import Popen, call

with open('ips.txt') as f:
    lineNumber = 1
    for line in f:
        lineNumber += 1
        programName = "example.exe"
        print(programName + " " + line.strip(' \t\n\r'))
        p = Popen([programName, line.strip(' \t\n\r')])		

        if lineNumber % 7 == 0:
            time.sleep(30)
		
		

				