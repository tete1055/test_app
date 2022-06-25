from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
  path('', views.IndexView, name='index'),
  path('<int:page>', views.IndexView, name='index'),
  path('posts/<int:pk>', views.createpost, name='posts'),
  path('posts/<int:pk>/<int:page>', views.createpost, name='posts'),
  path('mypage/', views.mypage, name='mypage'),
  path('good/', views.good, name='good'),
  path('delete/<int:delete_id>', views.delete, name='delete'),
  path('users/', views.users, name='users'),
  path('explain/', views.explain.as_view(), name='explain'),
]