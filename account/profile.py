from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import JsonResponse
from .models import Customer


from account.forms import ProfileForm, ChangePasswordForm


def profile_view(request):
    user = request.user
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            if len(data['phone_number']) != 11 or not (data['phone_number']).isdigit():
                return render(request, 'account/register.html', {'validation': 'not valid'})
            else:
                Customer.objects.filter(username=request.user.username).update(
                    first_name=data['first_name'], last_name=data['last_name'])
                user.phone_number = data['phone_number']
                user.address = data['address']
                user.save()
                if request.is_ajax():
                    message = {'message': 'edited your profile successfully!'}
                    return JsonResponse(message)
            print(user)
            return render(request, 'account/profile.html', {'form': form})
    else:
        data = {
             'first_name': user.first_name,
             'last_name': user.last_name,
             'phone_number': user.phone_number,
             'address': user.address
         }
    return render(request, 'account/profile.html', {'form': ProfileForm(initial=data)})


def change_password_view(request):
    if request.POST:
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.user.set_password(data['confirm_new_password'])
            request.user.save()
            user = authenticate(usernname=request.user.username, password=data['confirm_new_password'])
            login(request, user)

            print('successfullllllllllll')
            return HttpResponseRedirect(reverse('account:change_password'))
        else:
            return render(request,
                          'account/change_password.html',
                          {'form': form})
    else:
        return render(request,
                      'account/change_password.html',
                      {'form': ChangePasswordForm(request.user)})


def reset_password(request):
    pass