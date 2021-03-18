#!/usr/bin/env python
import time
import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(
    queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


# 模拟 复杂处理任务，每个点 暂停 1 秒
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

 
print("pid =====", os.getpid())

# 
# 把消息分发给下一个空闲工作者
channel.basic_qos(prefetch_count=1)


channel.basic_consume('task_queue', callback)
channel.start_consuming()
