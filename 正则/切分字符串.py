import re
Str = 'A  b   c'
c = Str.split(' ')
print(c)

result = re.split(r'\s+',Str)
print(result)


Str1 = 'a, b ; ,c, e'
M_result = re.split(r'[\s\,\;]+',Str1)

print(M_result)


print('sdf\tasdads')
print(r'sdf\tasdads')