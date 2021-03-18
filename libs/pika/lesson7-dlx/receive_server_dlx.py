#!/usr/bin/env python
import time
import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='dlxc', exchange_type='fanout')

print(' [*] Waiting for messages. To exit press CTRL+C')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue


channel.queue_bind(exchange='dlxc',
                       queue=queue_name)

# 模拟 复杂处理任务，每个点 暂停 1 秒
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

 
print("pid =====", os.getpid())

channel.basic_consume(queue_name, callback)
channel.start_consuming()
