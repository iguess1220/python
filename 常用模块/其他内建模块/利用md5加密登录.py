import hmac
userDict = {}
def Print():
    print('''
       1: Add user
       2: Mod password
       3: del user
       4: list
       5: save
       6: login
    '''
    )
def Rec():
    return input('请输入用户名称: ')
def Rec_pass():
    return input('请输入密码: ')
def ADD():
    newuser = Rec()
    if newuser in userDict.keys():
        print('此用户已存在')
    else:
        password = bytes(Rec_pass(),encoding='utf-8')
        userDict[newuser] = Sha(password)
def MOD():
    Getuser = Rec()
    if Getuser in userDict.keys():
        ModPass = bytes(Rec_pass(),encoding='utf-8')
        userDict[Getuser] = Sha(ModPass)
    else:
        print('没有此用户')
def View():
    print(userDict)
def Del():
    Deluser = Rec()
    if userDict[Deluser]:
        del userDict[Deluser]
        print('已删除用户 %s' %Deluser)
    else:
        print('没有此用户')
def Save():
    with open('passwd','w') as e:
        e.write(str(userDict))
def Read():
    global  userDict
    with open('passwd','r') as f:
        tc = f.read()
        userDict = eval(tc)
def Sha(arg):
    shapass = hmac.new(b'secret',arg,digestmod='sha256')
    return shapass.hexdigest()
def Login():
    L_user = Rec()
    L_password = bytes(Rec_pass(),encoding='utf-8')
    if userDict[L_user] != Sha(L_password):
        print('pass error')
    else:
        print('success')
# 1, 定义字典
# 2，打印功能  添加 修改 删除 查看
# 3, 添加：
# 4. 修改
# 5. 删除
# 6. 查看
# 7. 保存
# 8. 读取已有字典
# 加密:
Read()
while True:
    Print()
    N = input('input number: ')
    if N == '1':
        ADD()
    elif N == '2':
        MOD()
    elif N == '3':
        Del()
    elif N == '4':
        View()
    elif N == '5':
        Save()
    elif N == '6':
        Login()
    else:
        print('input error,please input again')
