from django.urls import path
from . import views


urlpatterns  =[
    path('a1/', views.register_view, name='register_url'),
    path('a2/', views.login_view, name='login_url'),
    path('a3/', views.logout_view, name='logout_url'),
]
