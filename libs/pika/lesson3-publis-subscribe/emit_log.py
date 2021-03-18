#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建 一个扇形的 交换器
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 消息
message = ' '.join(sys.argv[1:]) or "info: Hello world!"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
