from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from .models import Customer
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm, LoginForm, ProfileForm, ResetPasswordForm
from django.contrib.auth.views import password_reset


def register(request):
    if request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            if len(data['phone_number']) != 11 or not (data['phone_number']).isdigit():
                return render(request, 'account/register.html', {'validation': 'not valid'})
            else:
                customer = Customer.objects.create(first_name=data['first_name'],
                                                    last_name=data['last_name'],
                                                    username=data['username'])
                customer.set_password(data['password'])
                customer.phone_number = data['phone_number']
                customer.address = data['address']
                customer.save()
                print(customer)
                user = authenticate(username=customer.username, password=data['password'])

                login(request, user)

            return render(request, 'account/register.html', {'success': 'Yes'})
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        return render(request, 'account/register.html', {'form': CustomerForm()})


def login_view(request):
    # delete cash of username and password
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect(reverse('home'))
            else:
                return render(request, 'account/login.html', {'error': True})
        else:
            return render(request, 'account/login.html', {'form': form})
    else:
        return render(request, 'account/login.html', {'form': LoginForm()})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def reset_password_view(request):

    if request.POST:
        return password_reset(request,
                              from_email=request.POST.get('email'))
    else:
        return render(request, 'reset_password.html')
