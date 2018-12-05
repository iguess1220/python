import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code: ',r)


print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
output,err = p.communicate(b'set q=ma\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit Code: ',p.returncode)