# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-10 15:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='立项时间')),
                ('client', models.CharField(max_length=100, verbose_name='委托单位')),
                ('town', models.CharField(max_length=100, verbose_name='所在镇')),
                ('place', models.CharField(max_length=100, verbose_name='地点')),
                ('contacts', models.CharField(max_length=100, verbose_name='联系人')),
                ('contacts_phone', models.CharField(max_length=100, verbose_name='联系电话')),
                ('name', models.CharField(max_length=100, verbose_name='项目名称')),
                ('description', models.TextField(verbose_name='项目描述')),
                ('project_status', models.IntegerField(choices=[(0, '新建的'), (1, '进行中'), (2, '暂停中'), (3, '已结项')], default=0, verbose_name='项目状态')),
                ('tender_status', models.IntegerField(choices=[(0, '未开始'), (1, '进行中'), (2, '已完成')], default=0, verbose_name='投标状态')),
                ('contract_status', models.IntegerField(choices=[(0, '未开始'), (1, '进行中'), (2, '已完成')], default=0, verbose_name='合同状态')),
                ('end_time', models.DateTimeField(blank=True, verbose_name='结项时间')),
                ('remark', models.CharField(blank=True, max_length=255, verbose_name='备注')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '项目详情',
                'verbose_name_plural': '项目详情',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='ProjectApproval',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='审批时间')),
                ('remark', models.CharField(blank=True, max_length=1000, verbose_name='审批备注')),
                ('result', models.IntegerField(choices=[(1, '通过'), (2, '驳回')], verbose_name='审批结果')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '项目审批',
                'verbose_name_plural': '项目审批',
            },
        ),
        migrations.CreateModel(
            name='ProjectAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('category', models.IntegerField(choices=[(1, '投标文件'), (2, '合同文件'), (3, '其他文件')], verbose_name='文件分类')),
                ('name', models.CharField(max_length=100, verbose_name='附件名')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '项目附件',
                'verbose_name_plural': '项目附件',
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('is_problem', models.IntegerField(default=0, verbose_name='是否为问题')),
                ('reply_to', models.IntegerField(verbose_name='回复对象')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('status', models.IntegerField(choices=[(-1, '待解决'), (0, '已解决'), (1, '未解决')], verbose_name='问题解决状态')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '项目评论',
                'verbose_name_plural': '项目评论',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('operate_to', models.CharField(max_length=100, verbose_name='操作对象')),
                ('action', models.IntegerField(choices=[(1, '编辑'), (2, '评审'), (3, '回复'), (4, '上传'), (5, '更新'), (6, '删除'), (999, '其他')], verbose_name='动作')),
                ('operate_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'verbose_name': '用户操作日志',
                'verbose_name_plural': '用户操作日志',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('expect_end_time', models.DateTimeField(auto_now_add=True, verbose_name='截止时间')),
                ('actual_end_time', models.DateTimeField(auto_now_add=True, verbose_name='实际结束时间')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('level', models.IntegerField(choices=[(1, '一般'), (2, '紧急'), (3, '十分紧急')], default=1, verbose_name='紧急程度')),
                ('status', models.IntegerField(choices=[(-1, '新建的'), (0, '已完结'), (1, '进行中')], default=-1, verbose_name='任务状态')),
                ('manager', models.CharField(max_length=10, verbose_name='负责人')),
                ('work_requirements', models.CharField(blank=True, max_length=500, verbose_name='任务要求')),
                ('other_requirements', models.CharField(blank=True, max_length=300, verbose_name='其他要求')),
                ('coordinate', models.IntegerField(choices=[(1, '坐标类型1'), (2, '坐标类型2'), (3, '其他')], default=1, verbose_name='采用坐标')),
                ('dimordinate', models.CharField(blank=True, max_length=30, verbose_name='坐标标注')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
        migrations.CreateModel(
            name='WorkAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('category', models.IntegerField(choices=[(1, '数据文件'), (2, '成果文件'), (3, '其他文件')], verbose_name='文件分类')),
                ('name', models.CharField(max_length=100, verbose_name='附件名')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '任务附件',
                'verbose_name_plural': '任务附件',
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='WorkPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('percent', models.CharField(blank=True, max_length=10, verbose_name='工作量百分比')),
                ('output', models.IntegerField(blank=True, verbose_name='工作量产值')),
                ('mode', models.IntegerField(choices=[(1, '外业'), (2, '内业')], default=1, verbose_name='作业方式')),
                ('remark', models.CharField(blank=True, max_length=200, verbose_name='备注')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'verbose_name': '任务人员分配',
                'verbose_name_plural': '任务人员分配',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='环节')),
            ],
            options={
                'verbose_name': '任务环节',
                'verbose_name_plural': '任务环节',
            },
        ),
        migrations.CreateModel(
            name='WorkRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='角色')),
            ],
            options={
                'verbose_name': '任务角色',
                'verbose_name_plural': '任务角色',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='类型')),
            ],
            options={
                'verbose_name': '任务类型',
                'verbose_name_plural': '任务类型',
            },
        ),
        migrations.AddField(
            model_name='workperson',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.WorkRole'),
        ),
        migrations.AddField(
            model_name='workperson',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workperson',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Work'),
        ),
        migrations.AddField(
            model_name='work',
            name='work_process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.WorkProcess'),
        ),
        migrations.AddField(
            model_name='work',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.WorkType'),
        ),
    ]
