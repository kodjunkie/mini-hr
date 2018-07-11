from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('edit-profile', views.edit, name='edit'),
    path('update-profile', views.update, name='update'),
    path('email-users', views.SendUserEmails.as_view(), name='email'),
]
