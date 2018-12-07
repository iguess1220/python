import base64
# Str = b'binary\x00string'
# ded = base64.b64encode(Str)
# print(ded)
# result = base64.b64decode(ded)
# print(result)

Bytes = b'i\xb7\x1d\xfb\xef\xff'
enBytes = base64.b64encode(Bytes)
print(enBytes) # 这种参数不能直接作为参数

url_enBytes = base64.urlsafe_b64encode(Bytes)
print(url_enBytes)
url_deBytes = base64.urlsafe_b64decode(url_enBytes)
print(url_deBytes)


test = b'abcd'
en_test = base64.b64encode(test)
print(en_test)


# 测试题

def safe_base64_decode(s):
    return base64.b64decode(s+(4-len(s)%4) * b'=')
print(safe_base64_decode(b'YWJjZA='))
