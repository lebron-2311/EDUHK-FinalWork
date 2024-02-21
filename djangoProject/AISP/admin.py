from django.contrib import admin
from .models import Student, Course, LearningResource, Teacher


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Student_Name', 'StudentID', 'email', 'classNum', 'grade', 'major', 'score']
    # 其他自定义选项
    search_fields = ['Student_Name', 'StudentID', 'email']
    list_filter = ['grade', 'major']
    ordering = ['score', 'grade']
    fieldsets = (
        ('Personal Information', {
            'fields': ('Student_Name', 'StudentID', 'email')
        }),
        ('Academic Information', {
            'fields': ('classNum', 'grade', 'major')
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['name']
    date_hierarchy = 'start_date'
    ordering = ['-start_date']
    list_per_page = 10
    # 其他自定义选项


@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    list_filter = ['course']
    search_fields = ['title']
    ordering = ['title']
    list_per_page = 20
    # 其他自定义选项


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['Teacher_name', 'TeacherID', 'email', 'classNum', 'subject', 'position', 'uploadScore']
    list_filter = ['classNum', 'subject', 'position']
    search_fields = ['Teacher_name', 'TeacherID', 'email']
    ordering = ['Teacher_name']
    readonly_fields = ['uploadScore']
    # 其他自定义选项
