
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

#### setup 

1. 创建 `blog/views.py` 完成 `helloWorld`函数
2. 配置路由，项目层次 与 应用层次 
    - 应用层次 `blog/urls.py`
    - 项目层次 `introduction/urls.py`
3. 应用添加到项目中 `introduction/settings`
    - INSTALLED_APPS
    - 添加 `blog.apps.BlogConfig`
4. 访问 `http://127.0.0.1:8000/blog/hello_world`


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
- 配置
    - `introduction/settings.py`
    - DATABASES
    
#### 创建文章模型

> 字段定义

- AutoField
- primary_key 属性

  
#### setup 

1. 在`blog/models.py`  中定义模型
2. 创建迁移 文件
    - 执行 `python manage.py makemigrations` 
    - 生成 `blog/migrations/0001_initial.py`
3. 执行迁移文件
    - 执行 `python manage.py migrate`
    

### shell

1. 启动 dango shell
   - `python manage.py shell`
2. 执行 命令

```shell
from blog.models import Article
a = Article()
a.title = 'test shell'
a.content = 'content '
#保存
a.save()

# 查询所有文章,校验 是否写入成功
articles = Article.objects.all()

article = articles[0]
print(article.title)

# 退出
exit()
```


### Admin 模块

- 后台管理工具
- 定义模型元数据


#### setup 

1. 创建超级管理员
    - `python manage.py createsuperuser`
2. 启动应用,访问管理界面
    - `http://127.0.0.1:8000/admin/`
3. 将 article 模型注册到 Admin 中
    - 编辑 `blog/admin.py`
    - 可在后台看见
4. 定义后台管理

### 页面渲染 

1. 编辑 `blog/views.py`
2. 配置 路由


### 视图与模板

1. 创建模板文件
    - `blog/templates`
2. 模板语言
    - `{% %}`
    - 语法
    
3. url 参数获取
