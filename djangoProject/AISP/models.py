from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Student(models.Model):
    Student_Name = models.CharField(max_length=100)  # 学生姓名
    StudentID = models.CharField(max_length=50)  # 学号
    email = models.EmailField(unique=True)  # 邮箱
    password = models.CharField(max_length=100)  # 密码
    classNum = models.CharField(max_length=100)  # 班级
    grade = models.CharField(max_length=50)  # 年级
    major = models.CharField(max_length=100)  # 专业
    score = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])  # 成绩，默认为0，范围为0到100
    # 其他学生相关的字段

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    # 其他课程相关的字段

    def __str__(self):
        return self.name


class LearningResource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='learning_resources/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # 其他学习资源相关的字段

    def __str__(self):
        return self.title


class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=100)  # 教师姓名
    TeacherID = models.CharField(max_length=100)  # 教师工号
    email = models.EmailField(unique=True)  # 教师邮箱
    password = models.CharField(max_length=100)  # 教师密码
    classNum = models.CharField(max_length=100)  # 教师带的班级
    subject = models.CharField(max_length=100)  # 教授的课程
    position = models.CharField(max_length=100)  # 教师职位
    uploadScore = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])  # 上传成绩字段，默认值为0.0

    # 其他教师相关的字段

    def __str__(self):
        return self.Teacher_name