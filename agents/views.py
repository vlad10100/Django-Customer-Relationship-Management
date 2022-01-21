from django.shortcuts import render, reverse

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin

class AgentListView(OrganizerAndLoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent_list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent_list')

class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent_list')