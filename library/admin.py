from django.contrib import admin

# Register your models here.
from library.models import *

admin.site.register(Usertype)
admin.site.register(User)
admin.site.register(Program)
admin.site.register(Semester)
# admin.site.register(Course)
admin.site.register(Note)
# admin.site.register(Syalabus)
# admin.site.register(OldQuestionPaper)
