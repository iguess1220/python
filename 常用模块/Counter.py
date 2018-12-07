from collections import Counter
c = Counter()
for ch in 'programing':
    c[ch] = c[ch]+1
print(c['r'])
