from django.urls import path, include
from exammanager import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('viewhall/', views.viewhall, name="viewhall"),
    path('admin/', views.admin, name="admin"),
    path('register/', views.register, name="register"),

]