from django.db import models
from datetime import datetime


class Teacher(models.Model):
    name = models.CharField(verbose_name='教师姓名', max_length=20)
    gender = models.CharField(choices=(('male','男'), ('female', '女')), verbose_name='性别', max_length=10, default='')
    image = models.ImageField(verbose_name='教师图片', max_length=100, upload_to='teacher/%Y/%m')
    work_year = models.IntegerField(verbose_name='工作年限', null=True, blank=True)
    introduction = models.CharField(max_length=100, verbose_name='教师描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', max_length=20)
    nick_name = models.CharField(default='', verbose_name='昵称', max_length=10)

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name
        db_table='教师'

    def __str__(self):
        return self.name


class   Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='课程名')
    description = models.CharField(max_length=100, verbose_name='课程描述')
    degree = models.CharField(choices=(('CJ', '初级'), ('ZJ', '中级'), ('GJ', '高级')), max_length=10)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    students_num = models.IntegerField(default=0, verbose_name='学习人数')
    category = models.CharField(max_length=20, verbose_name='课程类别')
    favor_num = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name='课程图片', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='课程添加时间')
    teacher = models.ForeignKey(Teacher, verbose_name="授课教师", blank=True, null=True)
    recommend = models.BooleanField(default=False, verbose_name='是否推荐', max_length=2)
    has_favor = models.BooleanField(default=False, verbose_name='是否收藏')
    notice = models.CharField(default='', verbose_name='课程须知', max_length=200)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        db_table = '课程'

    def __str__(self):
        return self.title


class Chapter(models.Model):
    name = models.CharField(max_length=50, verbose_name='章节名')
    course = models.ForeignKey(Course, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='课程添加时间')
    url = models.URLField(max_length=200, verbose_name='视频链接',null=True, blank=True)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        db_table = '章节'

    def __str__(self):
        return self.name



class CourseResource(models.Model):
    name = models.CharField(max_length=30, verbose_name='资料名称')
    course = models.ForeignKey(Course)
    download = models.FileField(upload_to='course/download/%Y/%m', verbose_name='下载', max_length=100)

    class Meta:
        verbose_name = '课程资源下载'
        verbose_name_plural = verbose_name
        db_table = '课程资源下载'

    def __str__(self):
        return self.name




