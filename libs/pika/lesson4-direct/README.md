```bash
## consumer1
# 创建随机队列 并绑定  info warning error 3个 routing
python receive_logs_direct.py info warning error


## consumer2
# 创建随机队列 并绑定  error 1个 routing
python receive_logs_direct.py error


## publisher
# 默认 info 信息， 只有  consumer1 处理
python emit_log_direct.py "Run. Run. Or it will explode."
# error 消息 两个 consumer 均接收
python emit_log_direct.py error "Run. Run. Or it will explode."
```