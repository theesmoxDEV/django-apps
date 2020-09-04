from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.model_form_upload, name='model_form_upload'),
    path('create_cloud/', views.create_cloud, name='create_cloud')
]
