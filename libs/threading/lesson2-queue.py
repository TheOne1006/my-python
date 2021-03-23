
# -*- coding: utf-8 -*-
import threading
import queue

maxThreads = 50

"""
通过队列的方式处理最大并发
"""

class store(threading.Thread):
    def __init__(self, store, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.store = store

    def run(self):
        try:
            print('This is store %s\n' % self.store)
        except Exception as e:
            print(e)
        finally:
            self.queue.get()
            self.queue.task_done()

def main():
    q = queue.Queue(maxThreads)
    for s in range(1500):
        q.put(s)
        t = store(s, q)
        t.start()
    q.join()
    print('over')

if __name__ == '__main__':
    main()