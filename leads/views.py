from django.shortcuts import render, redirect
from .models import Lead, Agent, User
from .forms import Lead_Form, Lead_Edit_Form


def home(request):
    lead = Lead.objects.all()
    context = {'leads':lead}
    return render(request, 'leads/home.html', context)

def retrieve(request):
    lead = Lead.objects.all()
    agent = Agent.objects.all() 
    context = {
        'lead': lead,
        'agent': agent
    }
    return render(request, 'leads/retrieve.html', context)


def create(request):
    form = Lead_Form()
    context = {'form':form}
    if request.method == 'POST':
        form = Lead_Form(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            agent = User.objects.get(username=agent)
            print(agent)
            agent = form.cleaned_data['agent']
            Lead.objects.create(first_name=first_name, last_name=last_name,
                                age=age, agent=agent)
            print('Successfully created')
    return render(request, 'leads/create.html', context)

def detail(request, pk):
    x = Lead.objects.get(id=pk)
    print(x)
    context = {'lead': x}
    return render(request, 'leads/detail.html', context)

def edit(request, pk):
    lead = Lead.objects.get(id=pk)
    form = Lead_Edit_Form()
    context = {'form':form}
    if request.method == 'POST':
        form = Lead_Edit_Form(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age 
            lead.save()
            return retrieve(request)

    return render(request, 'leads/edit.html', context)

def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/')

