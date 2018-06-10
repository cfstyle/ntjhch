from django.contrib import admin
from project.models import (
        Project,
        ProjectApproval,
        ProjectAttachment,
        ProjectComment,
        Record,
        WorkType,
        WorkProcess,
        WorkAttachment,
        WorkRole,
        Work,
        WorkPerson
    )
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

class ProjectApprovalAdmin(admin.ModelAdmin):
    pass

class ProjectAttachmentAdmin(admin.ModelAdmin):
    pass

class ProjectCommentAdmin(admin.ModelAdmin):
    pass

class RecordAdmin(admin.ModelAdmin):
    pass

class WorkTypeAdmin(admin.ModelAdmin):
    pass

class WorkProcessAdmin(admin.ModelAdmin):
    pass

class WorkAttachmentAdmin(admin.ModelAdmin):
    pass

class WorkRoleAdmin(admin.ModelAdmin):
    pass

class WorkAdmin(admin.ModelAdmin):
    pass

class WorkPersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectApproval, ProjectApprovalAdmin)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)
admin.site.register(ProjectComment, ProjectCommentAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(WorkType, WorkTypeAdmin)
admin.site.register(WorkProcess, WorkProcessAdmin)
admin.site.register(WorkAttachment, WorkAttachmentAdmin)
admin.site.register(WorkRole, WorkRoleAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(WorkPerson, WorkPersonAdmin)