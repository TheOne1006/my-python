## 系统配置

- 静态文件

## orm  常用字段

## 关系类型字段

- 关联表

### 元数据 `class Meta`

- 子类


### script

1. 数据迁移
2. 删除模型类
    - models.py
    - migrations
    - django_migrations 表
3. 初始化数据
    - `python orm_data.py`
    - `python manage.py dumpdata > import_data.json` 导出数据 
    - `python manage.py loaddata import_data.json` 导入数据


### ORM 操作

```python
# 加载 Teacher
from .models import AddressInfo, Teacher

# objects 是 对象模型类的 对象管理器
Teacher.objects
```