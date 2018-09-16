from django.conf.urls import url
from django.contrib import admin
from .views import CourseView



urlpatterns = [
    url(r'^courses/$', CourseView.as_view()),
    url(r'^courses/(?P<pk>\d+)/$', CourseView.as_view()),
]

