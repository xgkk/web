from django.urls import path,include
from django.conf.urls import url
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'iplist', views.UserViewSet)

# ip_list = views.UserViewSet.as_view({
#     'get': 'list'
# })

urlpatterns = [
    # path('ipusers/', views.download_ip_user),
    # path('ipuser/', views.ip_user),
    # path('', include(router.urls)),
    path('ipuser/', views.SnippetList.as_view()),
    # path('ipuser/<int:pk>', views.SnippetDetail.as_view()),
    # path('iplist/', ip_list, name='iplist'),

]
