#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.0.2'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

# 创建随机队列
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    print(f" bind queue:{queue_name}, routing:{binding_key}")
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue_name, callback, True)

channel.start_consuming()
