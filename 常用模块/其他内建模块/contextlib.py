from contextlib import contextmanager
@contextmanager
def tag(name):
    print('h1')
    yield  name#  with 语句先执行 yield之前的，调用yield时执行with语句内所以内容，最后执行yield之后的，为函数tag的顺序
    print('h2')
with tag('chenyang') as f:
    print('hello')
    print('world')
    print(f)

    """with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
"""
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.baidu.com') ) as page:
    for i in page:
        print(i)
    print(page)









