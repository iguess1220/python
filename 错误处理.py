try:
    print("try....")
    r = 10/0
    print('result:')
#except ZeroDivisionError as e:
except BaseException as e:
    print('result: ',e)
finally:
    print('finally')
# 后续语句print('result:', r)不会被执行，except由于捕获到ZeroDivisionError，因此被执行。最后，finally语句被执行。然后，程序继续按照流程往下走。


# 使用日志记录错误
import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except BaseException as e:
        logging.exception(e)
        with open('test.log','w') as f:
            f.write('asdf')
    finally:
        print("finally")
if __name__ == '__main__':
    main()
