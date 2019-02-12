#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
# from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

def project_attachment_path(instance, fname):
    ext = fname.split('.')[1]
    fname_ = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    return "project/attchments/{}".format(fname_)

# Create your models here.
class Project(models.Model):
    '''
    项目详情
    '''
    PROJECT_CODE = (
        (0, u'待审批'),
        (1, u'进行中'),
        (2, u'暂停中'),
        (3, u'已结项'),
        (4, u'已驳回')
    )
    TENDER_CODE = (
        (0, u'未开始'),
        (1, u'进行中'),
        (2, u'已完成')
    )
    CONTRACT_CODE = (
        (0, u'未开始'),
        (1, u'进行中'),
        (2, u'已完成')
    )

    id = models.CharField(u'项目编号', max_length=100, primary_key=True)
    create_time = models.DateTimeField(u'立项时间', auto_now_add=True)
    client = models.CharField(u'委托单位', max_length=100)
    town = models.CharField(u'所在镇', max_length=100)
    place = models.CharField(u'地点', max_length=100)
    contacts = models.CharField(u'联系人', max_length=100)
    contacts_phone = models.CharField(u'联系电话', max_length=100)
    name = models.CharField(u'项目名称', max_length=100)
    manager = models.ForeignKey(User)
    description = models.TextField(u'项目描述')
    project_status = models.IntegerField(u'项目状态', choices=PROJECT_CODE, default=0)
    tender_status = models.IntegerField(u'投标状态', choices=TENDER_CODE, default=0)
    contract_status = models.IntegerField(u'合同状态', choices=CONTRACT_CODE, default=0)
    end_time = models.DateTimeField(u'结项时间', blank=True, null=True)
    remark = models.CharField(u'备注', max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'项目详情'
        verbose_name_plural = u'项目详情'
        ordering = ['-create_time']

class ProjectApproval(models.Model):
    '''
    项目审批
    '''
    APPROVAL_STATUS = (
        (1, u'审批通过'),
        (2, u'审批驳回')
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    time = models.DateTimeField(u'审批时间', auto_now_add=True)
    remark = models.CharField(u'审批备注', max_length=1000, blank=True)
    user = models.ForeignKey(User)
    result = models.IntegerField(u'审批结果', choices=APPROVAL_STATUS)

    class Meta:
        verbose_name = u'项目审批'
        verbose_name_plural = u'项目审批'

class ProjectAttachment(models.Model):
    '''
    项目附件
    '''
    ATTACHMENT_CATEGORY = (
        (1, u'投标文件'),
        (2, u'合同文件'),
        (3, u'其他文件')
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    upload_time = models.DateTimeField(u'上传时间', auto_now_add=True)
    category = models.IntegerField(u'文件分类', choices=ATTACHMENT_CATEGORY)
    user = models.ForeignKey(User)
    name = models.FileField(u'附件名', upload_to=project_attachment_path)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = u'项目附件'
        verbose_name_plural = u'项目附件'
        ordering = ['-upload_time']

class ProjectComment(models.Model):
    '''
    项目评论
    '''
    PROBLEM_STATUS = (
        (-1, u'待解决'),
        (0, u'已解决'),
        (1, u'未解决')
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    time = models.DateTimeField(u'发表时间', auto_now_add=True)
    is_problem = models.IntegerField(u'是否为问题', default=0) # 1: 问题
    user = models.ForeignKey(User)
    reply_to = models.IntegerField(u'回复对象') #为空表示对项目进行评论，不为空表示回复对应的评论ID
    content = models.CharField(u'评论内容', max_length=300)
    status = models.IntegerField(u'问题解决状态', choices=PROBLEM_STATUS)

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = u'项目评论'
        verbose_name_plural = u'项目评论'
        ordering = ['-time']

class Record(models.Model):
    '''
    日志记录
    '''
    OPERATE = (
        (1, u'编辑'),
        (2, u'评审'),
        (3, u'回复'),
        (4, u'上传'),
        (5, u'更新'),
        (6, u'删除'),
        (999, u'其他'),
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    operate_time = models.DateTimeField(u'发表时间', auto_now_add=True)
    operate_to = models.CharField(u'操作对象', max_length=100)
    operate_user = models.ForeignKey(User)
    action = models.IntegerField(u'动作', choices=OPERATE)


    class Meta:
        verbose_name = u'用户操作日志'
        verbose_name_plural = u'用户操作日志'

class WorkType(models.Model):
    '''
    任务类型
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'类型', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'任务类型'
        verbose_name_plural = u'任务类型'

class WorkProcess(models.Model):
    '''
    任务环节
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'环节', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'任务环节'
        verbose_name_plural = u'任务环节'


class WorkAttachment(models.Model):
    '''
    任务附件
    '''
    ATTACHMENT_CATEGORY = (
    (1, u'数据文件'),
    (2, u'成果文件'),
    (3, u'其他文件')
    )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    upload_time = models.DateTimeField(u'上传时间', auto_now_add=True)
    category = models.IntegerField(u'文件分类', choices=ATTACHMENT_CATEGORY)
    user = models.ForeignKey(User)
    name = models.CharField(u'附件名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'任务附件'
        verbose_name_plural = u'任务附件'
        ordering = ['-upload_time']

class WorkRole(models.Model):
    '''
    任务角色字典表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'角色', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'任务角色'
        verbose_name_plural = u'任务角色'


class Work(models.Model):
    '''
    任务
    '''
    WORK_LEVEL = (
        (1, u'一般'),
        (2, u'紧急'),
        (3, u'十分紧急'),
        )
    WORK_STATUS = (
        (-1, u'新建的'),
        (0, u'已完结'),
        (1, u'进行中'),
        )
    COORDINATE_TYPE = (
        (1, u'坐标类型1'),
        (2, u'坐标类型2'),
        (3, u'其他'),
        )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    start_time = models.DateTimeField(u'开始时间', auto_now_add=True)
    expect_end_time = models.DateTimeField(u'截止时间', auto_now_add=True)
    actual_end_time = models.DateTimeField(u'实际结束时间', auto_now_add=True)
    title = models.CharField(u'标题', max_length=100)
    work_type = models.ForeignKey(WorkType)
    level = models.IntegerField(u'紧急程度', choices=WORK_LEVEL, default=1)
    status = models.IntegerField(u'任务状态', choices=WORK_STATUS, default=-1)
    work_process = models.ForeignKey(WorkProcess)
    manager = models.CharField(u'负责人', max_length=10)
    work_requirements = models.CharField(u'任务要求', max_length=500, blank=True)
    other_requirements = models.CharField(u'其他要求', max_length=300, blank=True)
    coordinate = models.IntegerField(u'采用坐标', choices=COORDINATE_TYPE, default=1)
    dimordinate = models.CharField(u'坐标标注', max_length=30, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'任务'
        verbose_name_plural = u'任务'


class WorkPerson(models.Model):
    '''
    任务人员分配
    '''
    OPERATION_MODE = (
    (1, u'外业'),
    (2, u'内业'),
    )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    work = models.ForeignKey(Work)
    user = models.ForeignKey(User)
    role = models.ForeignKey(WorkRole)
    percent = models.CharField(u'工作量百分比', max_length=10, blank=True)
    output = models.IntegerField(u'工作量产值', blank=True)
    mode = models.IntegerField(u'作业方式', choices=OPERATION_MODE, default=1)
    remark = models.CharField(u'备注', max_length=200, blank=True)


    class Meta:
        verbose_name = u'任务人员分配'
        verbose_name_plural = u'任务人员分配'
        ordering = ['-id']