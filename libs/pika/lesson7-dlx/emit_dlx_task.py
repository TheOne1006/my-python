#!/usr/bin/env python
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

#  ttl的单位是us，ttl=60000 表示 60s
arguments = {
    'x-message-ttl': 5 * 1000,
    'x-dead-letter-exchange': 'dlxc',
    'x-dead-letter-routing-key': 'dlxc'
}
# 普通服务
channel.queue_declare(queue='lesson_7', durable=True, arguments=arguments)

# 尝试获取输入文字
message = ' '.join(sys.argv[1:]) or 'Hello World'

# 推送消息
channel.basic_publish(exchange='',
                      routing_key='lesson_7',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 确保消息是持久的
                      ))

print(" [x] Sent %r" % message)
connection.close()
