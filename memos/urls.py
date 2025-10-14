from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'memos', views.MemoViewSet, basename='memo')

urlpatterns = [
    path('', include(router.urls)),
    path('me/', views.current_user, name='current_user'),
    path('register/', views.register_user, name='register_user'),
]