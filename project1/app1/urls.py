from django.urls import path
from . import views


urlpatterns = [
    path('a1/', views.student_view, name='student_url'),
    path('a2/', views.show_view, name='show_url'),
    path('a3/<int:pk>', views.update_view, name='update_url'),
    path('a4/<int:pk>', views.delete_view, name='delete_url'),
]


