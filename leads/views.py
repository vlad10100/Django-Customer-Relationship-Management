from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Lead, Agent, User
from .forms import Lead_Form, Lead_Edit_Form, CustomUser

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUser

    def get_success_url(self):
        return reverse('leads:login_view')



class LandingPageView(ListView):
    template_name = 'leads/home.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

class LeadListView(ListView):
    template_name = 'leads/retrieve.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadDetailView(DetailView):
    template_name = 'leads/detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    template_name = 'leads/create.html'
    form_class = Lead_Form
    
    def get_success_url(self):
        return reverse("leads:home")

    def form_valid(self, form):
        # Send an E-mail
        send_mail(
            subject = "A lead has been created.",
            message = "Go to the site to see the new lead.",
            from_email = "admin@admin.com",
            recipient_list = ['test@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    template_name = 'leads/edit.html'
    form_class = Lead_Edit_Form
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:home")

def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')


# def home(request):
#     lead = Lead.objects.all()
#     context = {'leads':lead}
#     return render(request, 'leads/home.html', context)

# def retrieve(request):
#     lead = Lead.objects.all() 
#     context = {
#         'lead': lead,
#     }
#     return render(request, 'leads/retrieve.html', context)

# def detail(request, pk):
#     x = Lead.objects.get(id=pk)
#     print(x)
#     context = {'lead': x}
#     return render(request, 'leads/detail.html', context)


# def create(request):
#     form = Lead_Form()
#     context = {'form':form}
#     if request.method == 'POST':
#         form = Lead_Form(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
#             agent = User.objects.get(username=agent)
#             print(agent)
#             agent = form.cleaned_data['agent']
#             Lead.objects.create(first_name=first_name, last_name=last_name,
#                                 age=age, agent=agent)
#             print('Successfully created')
#     return render(request, 'leads/create.html', context)


# def edit(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = Lead_Edit_Form()
#     context = {'form':form}
#     if request.method == 'POST':
#         form = Lead_Edit_Form(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age 
#             lead.save()
#             return retrieve(request)

#     return render(request, 'leads/edit.html', context)



