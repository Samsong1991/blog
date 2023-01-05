# @Time     : 2023/1/1 9:27 下午
# @Author   : Samsong
# @File     : urls.py
# @Description:


from django.conf.urls import url
from rest_framework import routers
from django.urls import include, path

from common import views
from common.views import ImageUploadViewSet

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)

app_name = 'common'

urlpatterns = [
    path('', include(router.urls)),
    url(r'^user/login', views.UserLoginViewSet.as_view()),
    url(r'^user/logout', views.UserLogoutViewSet.as_view()),
    url(r'^user/pwd', views.PasswordUpdateViewSet.as_view()),
    url(r'^dict', views.ConstantViewSet.as_view()),
    url(r'upload/$', ImageUploadViewSet.as_view())
]

