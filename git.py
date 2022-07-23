# Sync with Git
import subprocess
import sys
subprocess.run(['sudo', 'find', '.', '-name', "'*.sw*'", '|', 'sudo', 'xargs', '-i', 'rm', '{}'])
subprocess.run(['sudo', 'git', 'ls-files', '--modified', '|', 'sudo','xargs', 'git', 'add'])
subprocess.run(['sudo', 'git', 'ls-files', '--others', '|', 'sudo','xargs', 'git', 'add'])
subprocess.run(['sudo', 'git', 'commit', '-m', sys.argv[1]])
gitout = subprocess.run(['git', 'push', '--force', 'origin', 'main'])
with open('outputs.txt', 'a') as f:
 f.write("\n"+str(gitout)+"\n"+"========================================================================================================================================="+"\n")

