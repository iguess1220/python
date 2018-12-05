s = 'ABC\\-001'
print(s)
a = r'ABC\-001'#(r会忽略转义)
print(a)


import re
result = re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(result) # 匹配返回Match对象，不匹配返回None


test = input('请输入字符串: ')
#if re.match(r'^\d{11}\-\s?.?\d{3}.?\w{3}',test):
if re.match(r'^\d{11}@\d{3}.?\w{3}',test):
    print('ok')
else:
    print('failed')





