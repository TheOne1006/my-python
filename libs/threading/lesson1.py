from threading import Thread
from time import sleep, ctime


"""
定义函数sleep n 秒
"""
def func(name, sec):
    print('---开始---', name, '时间', ctime())
    sleep(sec)
    print('***结束***', name, '时间', ctime())


# 创建 Thread 实例

# 创建Thread实例，传递给他一个函数
t1 = Thread(target=func, args=('第一个线程', 1))
t2 = Thread(target=func, args=('第二个线程', 2))

# 启动线程运行
t1.start()
t2.start()

# 等待所有线程执行完毕
t1.join()  # join() 等待线程终止，要不然一直挂起
t2.join()