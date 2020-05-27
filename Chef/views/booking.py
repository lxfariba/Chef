from django.shortcuts import render, HttpResponseRedirect, redirect
from Chef.models import Booking, Table
from account.models import Customer
from Chef.forms import ReservationForm, EventForm, TableForm


def reservation_view(request):
    user = request.user
    if request.POST:
        form = ReservationForm(request.POST)
        data = form.cleaned_data

        if form.is_valid():
            print("here1")
            # if data['seats'] < data['number_of_people'] or not (data['number_of_people'].is_digit()):
            #     return render(request, 'Chef/reservation.html', {'validation': 'not valid'})
            booking = Booking.objects.create(number_of_people=data['number_of_people'],
                                             seats=data['seats'],
                                             dining_date=data['dining_date'],
                                             dining_time=data['dining_time'],
                                             )
            # booking.set_table(seats=data['seats'],
            #                   locate_table=data['locate_table'],
            #                   max_size=data['max_size'])
            # booking.set_event(party=data['party'],
            #                   event_name=data['event_name'])
            booking.save()
            print("here2")
            return render(request, 'Chef/reservation.html', {'Ok': True})

        else:
            return render(request, 'Chef/reservation.html', {'form': form})
    else:
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number
        }

        return render(request, 'Chef/reservation.html', {'form': ReservationForm(initial=data)})