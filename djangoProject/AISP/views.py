from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def student_view(request):
    # 处理学生页面的逻辑
    return HttpResponse("This is the student page.")


def teacher_view(request):
    # 处理教师页面的逻辑
    return HttpResponse("This is the teacher page.")


def guest_view(request):
    # 处理访客页面的逻辑
    return HttpResponse("This is the guest page.")
