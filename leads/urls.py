from django.urls import path  
from . import views 

app_name = 'leads'

urlpatterns = [
    path('', views.home, name='home'),
    path('retrieve/', views.retrieve, name='retrieve'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete')
]