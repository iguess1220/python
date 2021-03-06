"""
'\d' # 一个数字
'\w' #一个字母或数字
'\d{3,5}' # 3到5个数字
'12\w{5}' # 12和5个字母或数字
'.*' #  任意字符任意个数
'.+' 至少一个任意字符
'.?' 表示0个或1个
"""
# 如果匹配 "'010-12345'"  则是: \d{3}\-\d{3,8}

"""
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。


A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。

"""