from django.urls import path  
from . import views 
from .views import LandingPageView, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView

app_name = 'leads'

urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path('retrieve/', LeadListView.as_view(), name='retrieve'),
    path('detail/<int:pk>', LeadDetailView.as_view(), name='detail'),
    path('create/', LeadCreateView.as_view(), name='create'),
    path('edit/<int:pk>', LeadUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.delete, name='delete')
]