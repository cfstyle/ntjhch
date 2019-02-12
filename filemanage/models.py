#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
import uuid

# some functions here

def save_file_path(instance, fname):
    ext = fname.split('.')[1]
    fname_ = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    return "project/attchments/{}".format(fname_)

# Create your models here.
class File(models.Model):
    '''
    文件
    '''
    FILE_FORMAT_CATEGORY = (
        (1, u'图片'),
        (2, u'文档'),
        (3, u'音乐'),
        (4, u'视频'),
        (5, u'压缩包'),
        (6, u'数据文件'),
        (7, u'可执行文件'),
        (8, u'其他'),
    )

    id = models.AutoField(primary_key=True)
    file_path = models.FileField(u'文件名', upload_to=save_file_path)
    file_name = models.CharField(u'文件名', max_length=100, blank=True)
    file_name_origin = models.CharField(u'原始文件名', max_length=100, blank=True)
    file_size = models.IntegerField(u'文件大小', default=0)
    file_format = models.IntegerField(u'文件格式', choices=FILE_FORMAT_CATEGORY)
    upload_user = models.ForeignKey(User)
    upload_time = models.DateTimeField(u'上传时间', auto_now_add=True)

    def __str__(self):
        return str(self.file_name_origin)

    class Meta:
        verbose_name = u'文件'
        verbose_name_plural = u'文件'
        ordering = ['-upload_time']