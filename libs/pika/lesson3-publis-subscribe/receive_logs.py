#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 确认log 交换器
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 开启随机队列
# exclusive=True 当与消费者（consumer）断开连接的时候，这个队列应当被立即删除
result = channel.queue_declare('', exclusive=True)

# 获取随机队列名
queue_name = result.method.queue

print(f"queuename is: {queue_name}")


channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue_name, callback, True)

channel.start_consuming()
