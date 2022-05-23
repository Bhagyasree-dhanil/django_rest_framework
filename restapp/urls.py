'''
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('add/', views.add_item, name="add"),
]
'''

from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register(r"items", ItemViewSet )

urlpatterns=[
    path('', include(router.urls))
]
