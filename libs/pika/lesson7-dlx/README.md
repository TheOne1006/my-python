```bash
## 接受服务
python receiver_server.py

## dlx 服务
python receiver_server_dlx.py

# 请求, 正常接收
python emit_dlx_task.py 'hello...'

# 关闭 receiver_server.py

# 再次发送， 120s 以后
python emit_dlx_task.py 'hello dlx'

```