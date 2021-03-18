#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# durable 持久化
channel.queue_declare(queue='task_queue', durable=True)

# 尝试获取输入文字
message = ' '.join(sys.argv[1:]) or 'Hello World'

# 推送消息
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 确保消息是持久的
                      ))
print(" [x] Sent %r" % message)
connection.close()
