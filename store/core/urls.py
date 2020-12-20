from django.urls import path

from . import views

urlpatterns = [
    path('level1/', views.level1, name='level1'),
]
