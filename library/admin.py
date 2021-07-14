from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from library.models import *


@admin.register(Program)
class Program(admin.ModelAdmin):
    list_display = ['program_name', 'semesters']

    def semesters(self, obj):
        return format_html('<br/>'.join([p.semester for p in obj.semester.all()]))


admin.site.register(Semester)


@admin.register(Subject)
class Program(admin.ModelAdmin):
    list_display = ['subject_name', 'program_name', 'semester']


@admin.register(Note)
class Note(admin.ModelAdmin):
    list_display = ['subject', 'program_name', 'semester', 'file', 'added_by', 'date_of_added']
    search_fields = ('subject__subject_name',)
    list_filter = ('subject',)


@admin.register(Syllabus)
class Syllabus(admin.ModelAdmin):
    list_display = ['program_name', 'semester', 'subject', 'subject_code', 'credit_hrs', 'added_by', 'date_of_added']
    search_fields = ('semester__semester','program_name__program_name',)
    list_filter = ('semester__semester','program_name__program_name',)

    # def get_form(self, request, obj=None, **kwargs):
    #     current_user = request.user
    #     if not current_user.is_staff:
    #         self.exclude = ('added_by',)
    #         self.list_display = ('name', 'finish')
    #     form = super(Syllabus, self).get_form(request, obj, **kwargs)
    #     form.current_user = current_user
    #     return form



@admin.register(OldQuestionPaper)
class Note(admin.ModelAdmin):
    list_display = ['program_name', 'semester', 'subject', 'file', 'added_by', 'date_of_added']
    search_fields = ('semester__semester', 'program_name__program_name', 'added_by',)
    list_filter = ('semester__semester', 'program_name__program_name','added_by',)
