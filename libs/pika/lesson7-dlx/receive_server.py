#!/usr/bin/env python
import time
import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

arguments = {
    'x-message-ttl': 5 * 1000,
    'x-dead-letter-exchange': 'dlxc',
    'x-dead-letter-routing-key': 'dlxc'
}

channel.queue_declare(
    queue='lesson_7', durable=True, arguments=arguments)

print(' [*] Waiting for messages. To exit press CTRL+C')


# 模拟 复杂处理任务，每个点 暂停 1 秒
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

 
print("pid =====", os.getpid())


channel.basic_consume('lesson_7', callback)
channel.start_consuming()
