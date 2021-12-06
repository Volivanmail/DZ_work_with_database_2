from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Student, StudentAdmin)
# admin.site.register(Teacher, TeacherAdmin)
