
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


### 新增一个应用

```shell
# 建立 blog app
python manage.py startapp blog

# 产生目录
blog 
├── __init__.py
├── admin.py # 管理 模块
├── apps.py  # 声明应用
├── migrations #
│   └── __init__.py
├── models.py 
├── tests.py
├── urls.py
└── views.py
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
  
## setup

1. 创建 `blog/views.py` 完成 `helloWorld`函数
2. 配置路由，项目层次 与 应用层次 
    - 应用层次 `blog/urls.py`
    - 项目层次 `introduction/urls.py`
3. 应用添加到项目中 `introduction/settings`
    - INSTALLED_APPS
    - 添加 `blog.apps.BlogConfig`
4. 访问 `http://127.0.0.1:8000/blog/hello_world`