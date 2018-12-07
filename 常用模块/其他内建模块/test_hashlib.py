import hashlib
md5 = hashlib.md5()
#md5.update('how to use md5 in python hashlib?' .encode('utf- 8'))
# print(md5.hexdigest())
md5.update('how to use'.encode('utf-8'))
md5.update(' md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


sha1 = hashlib.sha256()
sha1.update('how to use sha in python hashlib?' .encode('utf-8'))
print(sha1.hexdigest())

mypassword = hashlib.sha256()
mypassword.update('20140916x'.encode('utf-8'))
print(mypassword.hexdigest())

