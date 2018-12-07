import hashlib
def Sha(arg):
    shapass = hashlib.sha256()
    shapass.update(arg.encode('utf-8'))
    return shapass.hexdigest()

print(Sha('cy'))