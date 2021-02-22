
- 基本命令
- 创建项目
- 项目目录


## 基础命令

```shell
# 查看常用命令
django-admin
```

- startproject 创建项目
- startapp 启动应用
- check 校验完整性
- runserver 启动环境
- shell 
- test 测试
- makemigrations 创建迁移文件
- migrate 执行迁移文件
- dumpdata 把数据库导出到文件
- loaddata 把数据库导入到数据库中

### 创建一个项目

```shell
django-admin startproject introduction

# 目录
#introduction
#├── introduction
#│   ├── __init__.py
#│   ├── asgi.py
#│   ├── settings.py 配置文件
#│   ├── urls.py 路由文件
#│   └── wsgi.py wsgi 应用
#└── manage.py 管理文件
```

可能还需要   
`apps.py` 应用  
`models.py` 视图处理  
`admin.py` 定义管理模型

启动项目
```shell
cd introduction

python manage.py runserver
```



## MVC


### 视图

- 模板 + 变量

### 模型层
- 模型层是什么？
    - 位于视图和数据之间
    - python 对象和数据库表之间的转换
- 模型层的作用
    - 屏蔽不同数据库的差异
    - 让开发者更专注于逻辑开发 
    - 提供更多便捷工具