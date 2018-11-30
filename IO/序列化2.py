import json
import pickle
d = dict(name='chenyang',age=30,score=90)
j_str = json.dumps(d)
f = open('test','w')
json.dump(j_str,f)
f.close()

e = open('test','r')
result2 = json.load(e)
e.close()
print(result2)