import os

c = os.path.abspath('.')
print(c)
try:
    os.mkdir('testdir')
except FileExistsError as e:
    print("error: %s" % e)
os.chdir('testdir')
if  'testone' not in os.listdir('.'):
    os.mkdir('testone')
print(os.listdir('.'))
#os.rmdir('testdir')
"""删除目录，不可递归"""
os.rmdir('testdir/testone')
os.rmdir('testdir')
