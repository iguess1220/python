import  os
from multiprocessing import Process
# print('Process %s start' % os.getpid())
# pid = os.fork()  # 会fork出一个子进程，并返回了两个值，子进程返回0，父进程返回子进程的id
# print(pid)
# # if pid == 0 :
#     print('I am child process %s and my parent is %s' % (os.getpid(),os.getppid()))
#     print(pid)
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#     print(pid)

# def run_proc(name):
#     print('run child process %s (%s) ...' %(name, os.getpid()))
#
# if __name__ == '__main__':
#     print('parent process %s ' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child porcess end')


from multiprocessing import Pool
import time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')








