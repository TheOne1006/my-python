#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.0.2'))  
# # docker container ip address
channel = connection.channel()

# 确认交换机 以及 交换机类型
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# 创建随机队列
result = channel.queue_declare('',exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    print(f" bind queue:{queue_name}, routing:{severity}")
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(cb, method, properities, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue_name, callback, True)

channel.start_consuming()
