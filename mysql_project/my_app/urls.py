from django.urls import path,include
from . import views
from rest_framework import routers
app_name ="my_app"
router = routers.DefaultRouter()
router.register('my_app', views.PostView)
urlpatterns = [
    path('', include(router.urls)),
    path('', views.article_list, name = 'list'),
    path('create/',views.article_create,name = 'create'),
    path('<slug:slug>/', views.article_detail,name = 'detail'),


]
