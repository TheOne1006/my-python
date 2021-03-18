#!/usr/bin/env python
import pika

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.2')) # docker container ip address

# 创建通道
channel = connection.channel()

# 确认 或 创建 队列 hello
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 订阅 hello
channel.basic_consume('hello', callback, True)

print(' [*] Waiting for messages. To exit press CTRL+C')

# 我们运行一个用来等待消息数据并且在需要的时候运行回调函数的无限循环
channel.start_consuming()
