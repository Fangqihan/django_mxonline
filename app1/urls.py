from django.conf.urls import url
from .views import CourseView, LoginView


urlpatterns = [
    url(r'^courses/$', CourseView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^courses/(?P<pk>\d+)/$', CourseView.as_view()),
]

