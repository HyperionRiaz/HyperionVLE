from django.contrib import admin
from moocadmin.models import Student, Course, Tutor, University, TaskFile, Task

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(University)
admin.site.register(TaskFile)
admin.site.register(Task)
# Register your models here.
