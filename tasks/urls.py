from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<str:pk>/', views.UpdateTask, name='update'),
    path('delete/<str:pk>/', views.DeleteTask, name='delete'),

]