# try:
#     f = open('test1.txt','r')
#     f.read()
#     #f.write('hello,world')
#     f.close()
# except FileNotFoundError as e:
#         print('error: %s' % e)
# finally:
#     print('hello,world')
import  time
# 合理读取 文件内容，使用for 遍历 readlines, 输出i.strip() 会去除掉 "\n"
# with open('test.txt','r') as file:
#     for i in file.readlines():
#         print(i.strip())

# 打开一个二进制文件，图片
# f = open('/Users/cy/Pictures/wonder-woman-8k-hd.jpg','rb')
# print(f.read())

# 字符编码

#with open("text.txt",'w',encoding='gbk') as f:

#     f.write('测试')

with open('text.txt','r',encoding='gbk') as e:
    c = e.read()
    print(c)



