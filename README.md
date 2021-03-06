# **NTJHCH项目管理系统**

## 需求

- 用户权限管理（登录）
- 用户登录后进行项目立项（项目情况、招投标情况、合同情况）
  - 项目名称、项目编号、委托单位、立项时间、投标文件、合同文件、其他文件（如设计文件、上级批文等）
  - 投标文件、合同文件以word文件为主，其他文件包含word、jpg、dwg等多种形式
  - 支持相关用户文件上传、下载、预览
  - 需要提交给领导审批
- 项目立项审批通过后，对应用户填写出项目单
  - 项目单填写和详情页面展示
  - 需要提交给领导审批
- 出项目单审批通过后，用户进行外业测量工作（工作管理），过程中或完成后录入项目外业测量数据和对应成果文件
  - 支持相关用户上传、下载
  - 数据文件格式有：.DAT、.CSV、.XLS等
  - 成果文件格式有：.PDF、.DWG、.JPG、.DOC等
- 领导对项目进行质量检查和验收
  - 细分为过程检查、最终检查、验收三个过程
  - 记录质量问题、质量判定、处理方法
- 所有上传文件的功能都要支持更新（替换）或历史记录保留
- 通过项目编号、项目名称、合同编号等查询到对应项目下的各类文件



## 表结构设计

- 项目详情表

  project

  | 字段            | 类型     | 长度 | 默认为空 | 备注           |
  | --------------- | -------- | ---- | -------- | -------------- |
  | id              | varchar  | 50   | 否       | 项目编号，主键 |
  | name            | varchar  | 100  | 否       | 项目名称       |
  | create_time | datetime |      | 否       | 立项时间       |
  | client          | varchar  | 100  | 否       | 委托单位       |
  | town               | varchar | 100 | 否 | 所在镇                        |
  | place              | varchar | 100 | 否 | 地点                          |
  | contacts           | varchar | 100 | 否 | 联系人                        |
  | contacts_phone     | varchar | 100 | 否 | 联系电话                      |
  | description     | varchar  | 2000 | 否       | 项目描述       |
  | project_status  | int      | 1    | 否       | 项目状态       |
  | tender_status   | int      | 1    | 否       | 投标状态       |
  | contract_status | int      | 1    | 否       | 合同状态       |
  | remark          | varchar  | 255  | 是       | 备注           |
  | end_time        | datetime |      | 是       | 结项时间       |
  | manager |  | |  | 项目负责人 |

  ​

- 项目审批情况表

  project_approval

  | 字段    | 类型     | 长度 | 默认为空 | 备注                     |
  | ------- | -------- | ---- | -------- | ------------------------ |
  | id      | int      | 10   | 否       | 主键，自增               |
  | project |          |      |          | 项目编号，外键project表  |
  | time    | datetime |      | 否       | 审批时间                 |
  | remark  | varchar  | 1000 | 否       | 审批备注                 |
  | user    |          |      |          | 审批人，外键User         |
  | result  | int      | 1    | 否       | 审批结果（通过、不通过） |

  ​

- 项目附件表（各类文件）
  project_attachment

  | 字段        | 类型     | 长度 | 默认为空 | 备注                    |
  | ----------- | -------- | ---- | -------- | ----------------------- |
  | id          | int      | 10   | 否       | 主键，自增              |
  | project     |          |      |          | 项目编号，外键project表 |
  | upload_time | datetime |      | 否       | 上传时间                |
  | category    | int      | 2    | 否       | 文件分类                |
  | user        |          |      |          | 所属人，外键User        |
  | name        | varchar  | 100  | 否       | 附件名                  |

- 项目评论表

  project_comment

  | 字段       | 类型     | 长度 | 默认为空 | 备注                                                         |
  | ---------- | -------- | ---- | -------- | ------------------------------------------------------------ |
  | id         | int      | 10   | 否       | 主键，自增                                                   |
  | project    |          |      |          | 项目编号，外键project表                                      |
  | time       | datetime |      | 否       | 发表时间                                                     |
  | is_problem | int      | 1    | 否       | 是否为问题                                                   |
  | user       |          |      |          | 发表人，外键User表                                           |
  | reply_to   | int      | 10   | 是       | 回复对象，为空表示对项目进行评论，不为空表示回复对应的评论ID |
  | status     | int      | 1    | 否       | 解决状态（如果评论被标记为问题），default=-1                 |
  | content    | varchar  | 255  |          | 内容                                                         |

- 日志记录表

  record

  | 字段         | 类型     | 长度 | 默认为空 | 备注                                             |
  | ------------ | -------- | ---- | -------- | ------------------------------------------------ |
  | id           | int      | 10   | 否       | 主键，自增                                       |
  | project      |          |      |          | 项目编号，外键project表                          |
  | operate_time | datetime |      | 否       | 操作时间                                         |
  | operate_to   | varchar  | 100  | 否       | 操作对象（文件、项目等）                         |
  | operate_user |          |      |          | 操作人，外键User                                 |
  | action       | int      | 2    | 否       | 动作类型（编辑、评审、回复、上传、更新、删除等） |


- 任务表

  work

  | 字段               | 类型     | 长度 | 默认为空 | 备注                          |
  | ------------------ | -------- | ---- | -------- | ----------------------------- |
  | id                 | int      | 10   | 否       | 主键，自增                    |
  | project            |          |      |          | 关联的项目编号，外键project表 |
  | create_time        | datetime |      | 否       | 任务创建时间                  |
  | start_time         | datetime |      | 否       | 任务开始时间                  |
  | expect_end_time    | datetime |      | 否       | 任务截止时间                  |
  | actual_end_time    | datetime |      | 是       | 任务实际结束时间              |
  | title              | varchar  | 200  | 否       | 任务标题                      |
  | work_type          |          |      |          | 任务类型 外键                 |
  | level              | int      | 1    | 否       | 紧急程度 1 2 3                |
  | status             | int      | 1    | 否       | 任务状态                      |
  | work_process       |          |      |          | 任务环节 外键                 |
  | manager            |          |      |          | 任务负责人                    |
  | work_requirements  |          |      |          | 任务要求                      |
  | other_requirements |          |      |          | 其他要求                      |
  | coordinate         |          |      |          | 采用坐标                      |
  | dimordinate        |          |      |          | 坐标标注                      |
  | remark             |          |      |          | 备注（仪器使用 作业方法  ）   |

- 任务附件表（各类文件）
  work_attachment

  | 字段        | 类型     | 长度 | 默认为空 | 备注             |
  | ----------- | -------- | ---- | -------- | ---------------- |
  | id          | int      | 10   | 否       | 主键，自增       |
  | work        |          |      |          | 任务编号，外键   |
  | upload_time | datetime |      | 否       | 上传时间         |
  | category    | int      | 2    | 否       | 文件分类         |
  | user        |          |      |          | 所属人，外键User |
  | name        | varchar  | 100  | 否       | 文件名           |

- 任务类型表

  work_type

  | 字段 | 类型    | 长度 | 默认为空 | 备注     |
  | ---- | ------- | ---- | -------- | -------- |
  | id   | int     | 10   | 否       | 主键     |
  | name | varchar | 100  | 否       | 任务类型 |

- 任务环节表

  work_process

  | 字段 | 类型    | 长度 | 默认为空 | 备注     |
  | ---- | ------- | ---- | -------- | -------- |
  | id   | int     | 10   | 否       | 主键     |
  | name | varchar | 100  | 否       | 任务环节 |

- 任务人员角色分配表

  work_person

  | 字段    | 类型    | 长度 | 默认为空 | 备注                |
  | ------- | ------- | ---- | -------- | ------------------- |
  | id      | int     | 10   | 否       | 主键，自增          |
  | project    |         |      |          | 项目编号 外键       |
  | work    |         |      |          | 任务编号 外键       |
  | user    |         |      | 否       | 任务人员 外键       |
  | role    | varchar | 100  | 否       | 任务角色  外键      |
  | percent | varchar | 10   | 否       | 工作量百分比        |
  | output | int | 10   | 否       | 工作量产值        |
  | mode    | int     |      | 否       | 作业方式(外业 内业) |
  | remark  | varchar | 200  | 是       | 备注                |

- 任务角色字典表

  work_role

  | 字段 | 类型    | 长度 | 默认为空 | 备注       |
  | ---- | ------- | ---- | -------- | ---------- |
  | id   | int     | 10   | 否       | 主键，自增 |
  | name | varchar | 100  | 否       | 任务角色   |

  ​


## 工作流转流程

立项：创建工程项目

审批：审批不通过（驳回）、审批通过

任务：创建任务，关联项目、分配作业类型、作业人员等

任务处理：接收任务、处理任务、提交审批

结项

