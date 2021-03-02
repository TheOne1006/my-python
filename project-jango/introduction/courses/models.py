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
        # abstract = True
        # permissions = (('定义好的权限', '权限说明'),)
        # managed = False
        unique_together = ('address', 'note')  # ((),())
        # app_label = 'courses'
        # db_tablespace  # 定义数据库表空间的名字
