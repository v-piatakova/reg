from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('', views.dashboard, name='dashboard'),

]
