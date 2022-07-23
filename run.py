import sys
import datetime
import subprocess
file = "playbooks/" + str(sys.argv[1])
print(file)
run = subprocess.run(['sudo', 'ansible-playbook', file], capture_output = True)

file1 = (run.stdout).decode('utf-8')
print(file1)
ct = datetime.datetime.now()
with open('outputs.txt', 'a') as f:
    f.write("\n"+"Time: " + str(ct)+"\n"+"File: "+ str(file)+ "\n"+ str(file1)+ "\n\n"+".............................................................................."+"\n")
