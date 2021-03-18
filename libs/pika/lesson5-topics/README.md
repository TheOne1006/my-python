```bash
## 执行下边命令 接收所有日志
python receive_logs_topic.py "#"


#执行下边命令 接收来自”kern“设备的日志：
python receive_logs_topic.py "kern.*"

# 接收严重程度为 ”critical“ 和 "kern" 设备的日志
python receive_logs_topic.py "kern.*" "*.critical"



## publisher
python emit_log_topic.py "kern.critical" "A critical kernel error"

# error 消息 两个 consumer 均接收
python emit_log_topic.py "other.common" "other warning"
```