from django.db import models

# Create your models here.
class AddressInfo(models.Model):
    # id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    # pid = models.ForeignKey('self', null=True, blank=True, verbose_name="自关联")
    # https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/#django.db.models.ForeignKey
    pid = models.ForeignKey('AddressInfo', null=True, blank=True, on_delete=models.CASCADE, verbose_name="自关联")
    note = models.CharField(max_length=200, null=True, blank=True, verbose_name="说明")

    def __str__(self):  # __unicode__(self)
        return self.address

    class Meta:
        # 定义元数据
        db_table = 'address'
        # ordering = ['pid']  # 指定按照什么字段排序
        verbose_name = '省市县地址信息'
        verbose_name_plural = verbose_name
        # abstract = True （True 为基类，用于继承)
        # permissions = (('定义好的权限', '权限说明'),)
        # managed = False
        unique_together = ('address', 'note')  # ((),()) 联合唯一约束
        # app_label = 'courses'
        # db_tablespace  # 定义数据库表空间的名字


class Teacher(models.Model):
    """讲师信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    introduction = models.TextField(default="这位老师很懒，木有签名的说~", verbose_name="简介")
    fans = models.PositiveIntegerField(default="0", verbose_name="粉丝数")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "讲师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):  # Python2:__unicode__
        return self.nickname


class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE,
                                verbose_name="课程讲师")  # 删除级联
    type = models.CharField(choices=((1, "实战课"), (2, "免费课"), (0, "其它")), max_length=1,
                            default=0, verbose_name="课程类型")
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息表"
        get_latest_by = "created_at"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.get_type_display()}-{self.title}"  # 示例：实战课-Django零基础入门到实战
        # return "{}-{}".format(self.get_type_display(), self.title)  # 示例：实战课-Django零基础入门到实战


class Student(models.Model):
    """学生信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    course = models.ManyToManyField(Course, verbose_name="课程")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(choices=((1, "男"), (2, "女"), (0, "保密")), max_length=1,
                              default=0, verbose_name="性别")
    study_time = models.PositiveIntegerField(default="0", verbose_name="学习时长(h)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "学生信息表"
        ordering = ['age']
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    """助教信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    teacher = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="讲师")  # 删除置空
    hobby = models.CharField(max_length=100, null=True, blank=True, verbose_name="爱好")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "助教信息表"
        db_table = "courses_assistant"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class GroupConcat(models.Aggregate):
    """自定义实现聚合功能，实现GROUP_CONCAT功能"""

    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)'

    def __init__(self, expression, distinct=False, ordering=None, separator=',', **extra):
        super(GroupConcat, self).__init__(expression,
                                          distinct='DISTINCT ' if distinct else '',
                                          ordering=' ORDER BY %s' % ordering if ordering is not None else '',
                                          separator=' SEPARATOR "%s"' % separator,
                                          output_field=models.CharField(), **extra)
