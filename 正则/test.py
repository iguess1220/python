import  re
re_mail = re.compile('\w+?\.?\w+?@\w+\.com')
def is_valid_email(addr):
    if re_mail.match(addr):
        return True
    return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


#<Tom Paris> tom@voyager.org => Tom Paris
#bob@example.com => bob
# 将正则规则用括号圈起来，在后面的group可通过区段调用
re_namemail = re.compile(r'<?([\w+|\s]*)?>?[\w+|\s]*@(\w+.?\w{3})')
def name_of_email(Mail_addr):
    return re_namemail.match(Mail_addr).group(1)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
