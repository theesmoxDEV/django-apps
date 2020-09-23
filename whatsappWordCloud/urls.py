from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.model_form_upload, name='index'),
    path('create_cloud/', views.create_cloud, name='create_cloud'),
    path('how_to_export_a_whatsapp_chat/', views.how_to_export, name='how_to_export')
]
