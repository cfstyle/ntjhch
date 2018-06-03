#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Project(models.Model):
    '''
    项目详情
    '''
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField('立项时间', auto_now_add=True)
    client = models.CharField('委托单位', max_length=100)
    town = models.CharField('所在镇', max_length=100)
    place = models.CharField('地点', max_length=100)
    contacts = models.CharField('联系人', max_length=100)
    contacts_phone = models.CharField('联系电话', max_length=100)
    name = models.CharField('项目名称', max_length=100)
    manager = models.ForeignKey(User)
    description = models.TextField('项目描述')
    project_status = models.CharField('项目状态', max_length=100)
    tender_status = models.CharField('投标状态', max_length=100)
    contract_status = models.CharField('合同状态', max_length=100)
    end_time = models.DateTimeField('结项时间', blank=True)
    remark = models.CharField('备注', max_length=255, blank=True)

    class Meta:
        verbose_name = '项目详情'
        verbose_name_plural = '项目详情'
        ordering = ['-create_time']

class ProjectApproval(models.Model):
    '''
    项目审批
    '''
    APPROVAL_STATUS = (
        (1, '通过'),
        (2, '驳回')
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    time = models.DateTimeField('审批时间', auto_now_add=True)
    remark = models.CharField('审批备注', max_length=1000, blank=True)
    user = models.ForeignKey(User)
    result = models.IntegerField('审批结果', choices=APPROVAL_STATUS)

    class Meta:
        verbose_name = '项目审批'
        verbose_name_plural = '项目审批'

class ProjectAttachment(models.Model):
    '''
    项目附件
    '''
    ATTACHMENT_CATEGORY = (
        (1, '投标文件'),
        (2, '合同文件'),
        (3, '其他文件')
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    upload_time = models.DateTimeField('上传时间', auto_now_add=True)
    category = models.IntegerField('文件分类', choices=ATTACHMENT_CATEGORY)
    user = models.ForeignKey(User)
    name = models.CharField('附件名', max_length=100)

    class Meta:
        verbose_name = '项目附件'
        verbose_name_plural = '项目附件'
        ordering = ['-upload_time']

class ProjectComment(models.Model):
    '''
    项目评论
    '''
    PROBLEM_STATUS = (
        (-1, '待解决'),
        (0, '已解决'),
        (1, '未解决')
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    time = models.DateTimeField('发表时间', auto_now_add=True)
    is_problem = models.IntegerField('是否为问题', default=0) # 1: 问题
    user = models.ForeignKey(User)
    reply_to = models.IntegerField('回复对象') #为空表示对项目进行评论，不为空表示回复对应的评论ID
    content = models.CharField('评论内容', max_length=300)
    status = models.IntegerField('问题解决状态', choices=PROBLEM_STATUS)
    
    class Meta:
        verbose_name = '项目评论'
        verbose_name_plural = '项目评论'
        ordering = ['-time']

class Record(models.Model):
    '''
    日志记录
    '''
    OPERATE = (
        (1, '编辑'),
        (2, '评审'),
        (3, '回复'),
        (4, '上传'),
        (5, '更新'),
        (6, '删除'),
        (999, '其他'),
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    operate_time = models.DateTimeField('发表时间', auto_now_add=True)
    operate_to = models.CharField('操作对象', max_length=100)
    operate_user = models.ForeignKey(User)
    action = models.IntegerField('动作', choices=OPERATE)

    class Meta:
        verbose_name = '用户操作日志'
        verbose_name_plural = '用户操作日志'

class WorkType(models.Model):
    '''
    任务类型
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField('类型', max_length=100)

    class Meta:
        verbose_name = '任务类型'
        verbose_name_plural = '任务类型'

class WorkProcess(models.Model):
    '''
    任务环节
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField('环节', max_length=100)

    class Meta:
        verbose_name = '任务环节'
        verbose_name_plural = '任务环节'


class WorkAttachment(models.Model):
    '''
    任务附件
    '''
    ATTACHMENT_CATEGORY = (
    (1, '数据文件'),
    (2, '成果文件'),
    (3, '其他文件')
    )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    upload_time = models.DateTimeField('上传时间', auto_now_add=True)
    category = models.IntegerField('文件分类', choices=ATTACHMENT_CATEGORY)
    user = models.ForeignKey(User)
    name = models.CharField('附件名', max_length=100)

    class Meta:
        verbose_name = '任务附件'
        verbose_name_plural = '任务附件'
        ordering = ['-upload_time']

class WorkRole(models.Model):
    '''
    任务角色字典表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField('角色', max_length=100)

    class Meta:
        verbose_name = '任务角色'
        verbose_name_plural = '任务角色'


class Work(models.Model):
    '''
    任务
    '''
    WORK_LEVEL = (
        (1, '一般'),
        (2, '紧急'),
        (3, '十分紧急'),
        )
    WORK_STATUS = (
        (-1, '新建的'),
        (0, '已完结'),
        (1, '进行中'),
        )
    COORDINATE_TYPE = (
        (1, '坐标类型1'),
        (2, '坐标类型2'),
        (3, '其他'),
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    start_time = models.DateTimeField('开始时间', auto_now_add=True)
    expect_end_time = models.DateTimeField('截止时间', auto_now_add=True)
    actual_end_time = models.DateTimeField('实际结束时间', auto_now_add=True)
    title = models.CharField('标题', max_length=100)
    work_type = models.ForeignKey(WorkType)
    level = models.IntegerField('紧急程度', choices=WORK_LEVEL, default=1)
    status = models.IntegerField('任务状态', choices=WORK_STATUS, default=-1)
    work_process = models.ForeignKey(WorkProcess)
    manager = models.CharField('负责人', max_length=10)
    work_requirements = models.CharField('任务要求', max_length=500, blank=True)
    other_requirements = models.CharField('其他要求', max_length=300, blank=True)
    coordinate = models.IntegerField('采用坐标', choices=COORDINATE_TYPE, default=1)
    dimordinate = models.CharField('坐标标注', max_length=30, blank=True)

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'


class WorkPerson(models.Model):
    '''
    任务人员分配
    '''
    OPERATION_MODE = (
    (1, '外业'),
    (2, '内业'),
    )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    work = models.ForeignKey(Work)
    user = models.ForeignKey(User)
    role = models.ForeignKey(WorkRole)
    percent = models.CharField('工作量百分比', max_length=10, blank=True)
    output = models.IntegerField('工作量产值', blank=True)
    mode = models.IntegerField('作业方式', choices=OPERATION_MODE, default=1)
    remark = models.CharField('备注', max_length=200, blank=True)

    class Meta:
        verbose_name = '任务附件'
        verbose_name_plural = '任务附件'
        ordering = ['-id']