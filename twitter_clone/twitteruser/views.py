from django.db import models
from django.shortcuts import get_object_or_404, redirect, render, reverse
from twitteruser.models import MyCustomUser, Ticket
from twitteruser.forms import LogInForm, AddTicketForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils import timezone
# from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import reverse
# from django.shortcuts import get_object_or_404, render, redirect
# <QuerySet [{'id': 1, 'password': 'pbkdf2_sßha256$180000$K3EVAgsFJJre$Ny846uUEid6xQv+78ho+7HMyxtFfJu4VclGr/VrcsA4=', 'last_login': datetime.datetime(2020, 2, 22, 5, 52, 55, 431671, tzinfo=<UTC>), 'is_superuser': True, 'username': 'tamoya', 'first_name': '', 'last_name': '', 'email': 'tamoyashopkins@gmail.com', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2020, 2, 22, 4, 48, 52, 813739, tzinfo=<UTC>), 'favorite_color': 'Purple!', 'home_page': None, 'display_name': '', 'age': None}]>
# Create your views here.
# @staff_member_required

def login_view(request):
    if request.user.is_authenticated:
        print(request)
        return HttpResponseRedirect(f'/user/{request.user.id}')
    else:
        if request.method == 'POST':
            form = LogInForm(data=request.POST)

            if form.is_valid():
                login(request, form.get_user())
                return HttpResponseRedirect(f'/user/{request.user.id}')
        else:
            form = LogInForm()

        return render(request, 'login.html', {'form': form})


@login_required
def home_page_view(request, id):
    results = None
    if request.method == 'POST':
        if 'InProgress' in request.POST['SortBy']:
            results = Ticket.objects.filter(status='In Progress', assign_to_user_id=id)
        if 'Filed' in request.POST['SortBy']:
            results = Ticket.objects.filter(filed_by=id)
        if 'Completed' in request.POST['SortBy']:
            results = Ticket.objects.filter(status='Completed', assign_to_user_id=id)
        if 'NULL' in request.POST['SortBy']:
            results = Ticket.objects.filter(assign_to_user_id=request.user.id).order_by('-posted_date')
    print(request.GET)
    current_user_id = str(request.GET)

    current_user = MyCustomUser.objects.get(pk=id)

    all_tickets = Ticket.objects.values().order_by('-posted_date')
    for ticket in all_tickets:
        if ticket['assign_to_user_id']:
            get_name = MyCustomUser.objects.filter(id=ticket['assign_to_user_id'])
            for item in get_name:
                ticket['assign_to_user_name'] = item.username
        else:
            ticket['assign_to_user_name'] = ticket['assign_to_user_id']
    ticket_types = [
        ('All Tickets', all_tickets),
        ('User Tickets', results)]
    return render(request, 'home_page.html', {
        'ticket_types': ticket_types,
        'current_user': current_user})


@login_required
def add_ticket_view(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            ticket = form.save()
            if data['assign_to_user']:
                ticket.status = 'In Progress'
                ticket.filed_by = request.user
            else:
                ticket.filed_by = request.user
            ticket.save()
            return HttpResponseRedirect(f'/')

    form = AddTicketForm()
    return render(request, 'add_ticket.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(f'/')


@login_required
def create_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # create new user obj: {'first_name': 'Romeo', 'last_name': 'G', 'email': 'romeo@gmail.com', 'user_name': 'Romeo', 'password1': 'asdfRomeo', 'password2': 'asdfRomeo'}
            MyCustomUser.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                username = data['user_name'],
                password = data['password1'],
            )
            return HttpResponseRedirect(f'/')

    form = UserCreationForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
def ticket_detail_view(request, id):
    # Ticket(id, title, posted_date, description, status, filed_by, assign_to_user, completed_by)
    ticket = Ticket.objects.get(pk=id)
    current_user_id = request.user.id
    if ticket.assign_to_user and ticket.completed_by is None:
        ticket.status = 'In Progress'
        user_name = MyCustomUser.objects.get(pk=ticket.assign_to_user_id)
    else:
        user_name = None


    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        'current_user_id': current_user_id,
        'user_name': user_name})

@login_required
def edit_ticket_view(request, id):
    instance = Ticket.objects.get(pk=id)
    if request.method == 'POST':
        form = AddTicketForm(request.POST, instance=instance)
        form.save()
        return HttpResponseRedirect(reverse('ticket', args=(instance.id,)))

    form = AddTicketForm(instance=instance)
    return render(request, 'edit_ticket.html', {'form': form})

def ticket_completed_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status='Completed'
    ticket.completed_by=request.user
    ticket.save()
    return HttpResponseRedirect(f'/')

