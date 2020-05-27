from django import forms
from Chef.models import Booking
from datetimewidget.widgets import DateWidget, TimeWidget, DateTimeWidget
# from Chef.widgets import DateWidget


class ReservationForm(forms.Form):
    first_name = forms.CharField(max_length=502)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    number_of_people = forms.CharField(max_length=3)
    dining_time = forms.TimeField(widget=TimeWidget)
    dining_date = forms.DateTimeField(widget=DateWidget)
    party = forms.CharField(max_length=5)
    event_name = forms.CharField(max_length=100)
    # seats = forms.CharField(max_length=3)
    # max_size = forms.CharField(max_length=3)
    locate_table = forms.CharField(max_length=1)

    # class Meta:
    #     model = Booking
    #     fields = ('dining_date', 'dining_time')
    #
    dateOptions = {
            'format': 'dd/mm/yyyy',
            'auto close': True,
            'showMeridian': True
        }
    widgets = {
        # Use localization and bootstrap 4
        'dining_date':  DateWidget(options=dateOptions, attrs={'id': 'date_dining'})

        }

    timeOptions = {
        'format': 'HH:ii P',
        'auto close': True,
        'ShowMeridian': True
    }

    widgets = {
        'dining_time': TimeWidget(options=timeOptions, attrs={'id': 'time_dining'})
    }
    # widgets = {
    #         # Use localization and bootstrap 4
    #         'dining_date':  DateTimeWidget(attrs={'id': 'date_dining'}, usel10n=True, bootstrap_version=4)
    #
    #     }


class EventForm(forms.Form):
    party = forms.CharField(max_length=5)
    event_name = forms.CharField(max_length=100)


class TableForm(forms.Form):
    seats = forms.CharField(max_length=3)
    max_size = forms.CharField(max_length=3)
    locate_table = forms.CharField(max_length=1)


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

