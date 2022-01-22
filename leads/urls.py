from django.urls import path  

from . import views 
from .views import (Home, LandingPageView, LeadListView, 
                    LeadDetailView, LeadCreateView, LeadUpdateView, 
                    SignUpView, LeadDeleteView, AssignAgentView
                    )
from django.contrib.auth.views import (LoginView, LogoutView,                  
                                        PasswordResetView, PasswordResetDoneView,
                                        PasswordResetConfirmView, PasswordResetCompleteView
                                        )
app_name = 'leads'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landingpage'),
    path('home/', Home.as_view(), name='home'),
    path('retrieve/', LeadListView.as_view(), name='retrieve'),
    path('detail/<int:pk>', LeadDetailView.as_view(), name='detail'),
    path('create/', LeadCreateView.as_view(), name='create'),
    path('edit/<int:pk>', LeadUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', LeadDeleteView.as_view(), name='delete'),
    path('assign_agent/<int:pk>', AssignAgentView.as_view(), name='assign_agent'),




    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    

]