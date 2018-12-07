from collections import ChainMap
import os,argparse

defaults={
    'color': 'red',
    'user': 'guest'
}
paser = argparse.ArgumentParser()
paser.add_argument('-u','--user')
paser.add_argument('-c','--color')
namespace = paser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}

combined = ChainMap(command_line_args,os.environ,defaults)

print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
