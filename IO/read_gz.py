def w_write():
    with open('test.txt','w') as w:
        w.write('测试')
def opengz():
    import  gzip
    l = []
    with gzip.open('test.gz','rb') as f:
        for i in f.readlines():
            l.append(i)
        return l
