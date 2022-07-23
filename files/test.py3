import os
ok = os.system('pwd')
stream = os.popen('ls -la')
output = stream.readlines()
print(output)
