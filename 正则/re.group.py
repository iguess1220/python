import re
t = '19-05-30'
m = re.match(r'(0[0-9]|1[0-9]|2[0-3]|[0-9])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])\-(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])',t)
print(m.group(1,2,3))
c=m.groups()
print(c)



# 贪婪匹配是默认的
m = re.match(r'^(\d+)(0*)$','123467870000').groups()
print(m)
# 在+后加个？，为尽可能少的匹配
n = re.match(r'^(\d+?)(0*)$','1234545780000').groups()
print(n)


# 提前编译好正则表达式，便于复用
re_tel = re.compile(r'^1[2-9][0-9]{9}$')  # 生成正则规则对象
mynum = re_tel.match('17710890916').group(0)
print(mynum)