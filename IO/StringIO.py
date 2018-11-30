from io import StringIO

def Mem_str():
    Mem_value = StringIO()
    Mem_value.write('hello')
    Mem_value.write(',')
    Mem_value.write('world')
    result = Mem_value.getvalue() # getvalue(）可以获取存储的值
    print(result)

def  create_str():
    One = StringIO('hello!\nHi!\nGoodbye!')
    #c = One.getvalue()
    #print(c)
    while True:
        i = One.readline()
        if i == '':
            break
        print(i.strip())

def exm_strip():
    Str_1 = '010103050020450000'
    a = Str_1.strip('0')  # 去除头尾的这个字符
    print(a)
#exm_strip()
create_str()

"""如果我们要输入二进制数据，需要使用BytesIO"""


from io import  BytesIO
def test_By():
    f = BytesIO()
    f.write('测试'.encode('utf-8'))  # 编码
    return f.getvalue()
c = test_By()
e = c.decode('utf-8')   # 解码
print(e)
