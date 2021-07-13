from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from library.models import *

#
# admin.site.register(Usertype)
# admin.site.register(User)
admin.site.register(Program)

# class Program(admin.ModelAdmin):
#     list_display = ['program_name', 'semester']
#     list_filter = ('semester',)
#     def supervisors(self, obj):
#         return format_html('<br/>'.join([p.name for p in obj.supervisor.all()]))
# @admin.register(Program)
# class Program(admin.ModelAdmin):
#     list_display = ['program_name', 'semester']

# def program_name(self, obj):
#     return format_html('<br/>'.join([p.name for p in obj.program_name.all()]))

# def semester(self, obj):
#     return format_html('<br/>'.join([p.name for p in obj.semester.all()]))


admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Note)


# admin.site.register(Syllabus)
@admin.register(Syllabus)
class Syllabus(admin.ModelAdmin):

    # def subject(self,obj):
    #     return (obj.subject_name, obj.subject_code)
    list_display = ['subject']

    # subject.allow_html = True

    # list_display = ['title', authors]

    # def subject_code(self, obj):
    #     return format_html('<br/>'.join([p.subject_code for p in obj.subject.all()]))

    # def subject(self, obj):
    #     return format_html('<br/>'.join([p.name for p in obj.subject_code.all()]))


admin.site.register(OldQuestionPaper)
