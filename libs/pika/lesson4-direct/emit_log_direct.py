#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# 绑定 交换机 和队列的关系
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

print(" [x] pre Sent %r:%r" % (severity, message))

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
