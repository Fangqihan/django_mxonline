from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Course, UserInfo,Token
from django.shortcuts import render
import uuid
from app1.auth.auth import TokenAuth


class CourseSerializer(serializers.ModelSerializer):
    # 若存在连表查询，可以直接在此处使用
    degree = serializers.CharField(source='get_degree_display')
    teacher = serializers.CharField(source='teacher.name')
    chapters = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_chapters(self,obj):
        query_set = obj.chapter_set.all()
        return [{'title':item.name,'url':item.url} for item in query_set]


class CourseView(APIView):
    authentication_classes = [TokenAuth,]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '')
        ret = {'code':1000, 'data':None}
        try:
            if pk:
                course_obj = Course.objects.filter(id=pk).first()
                ser = CourseSerializer(instance=course_obj,many=False)
            else:
                course_list = Course.objects.all()
                ser = CourseSerializer(instance=course_list, many=True)

            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code']=1001
            ret['error'] = '获取课程失败'
        print(ret)
        return Response(ret)


def test(request):
    course_obj = Course.objects.all().first()
    return render(request,'test.html',locals())


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000}
        user = request.data.get('user','')
        pwd = request.data.get('pwd','')
        user_obj = UserInfo.objects.filter(username=user,password=pwd).first()
        if not user_obj:
            ret['code'] = 1001
            ret['error'] = "用户名或密码错误"
        else:
            token = str(uuid.uuid4())
            Token.objects.update_or_create(user_id=user_obj.id,defaults={'token':token})
            ret['token']= token
        return Response(ret)


