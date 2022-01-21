from django.urls import path 
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView, AgentDeleteView

app_name = 'agents'

urlpatterns = (
    path('list/', AgentListView.as_view(), name='agent_list'),
    path('create/', AgentCreateView.as_view(), name='agent_create'),
    path('detail/<int:pk>', AgentDetailView.as_view(), name='agent_detail'),
    path('update/<int:pk>', AgentUpdateView.as_view(), name='agent_update'),
    path('delete/<int:pk>', AgentDeleteView.as_view(), name='agent_delete')
)