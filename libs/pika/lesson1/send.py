#!/usr/bin/env python
import pika

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 创建渠道
channel = connection.channel()


# 需要确认服务于消费者的队列已经存在
# 存在则无需创建
channel.queue_declare(queue='hello')


# 空字符串表示的默认交换机
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()
