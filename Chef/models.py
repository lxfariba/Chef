from django.db import models
from django.forms import ModelForm
from account.models import Customer


class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='food/galley_images')

    # def __str__(self):
    #     pass


class Table(models.Model):
    TABLE = (
        ('1', 'Inside'),
        ('2', 'Outside'),
    )
    seats = models.IntegerField(default=1)
    max_size = models.IntegerField(default=2)
    locate_table = models.CharField(max_length=1, choices=TABLE, blank=True)


# class TableForm(ModelForm):
#     class Meta:
#         model = Table
#         fields = ['seats', 'max_size', 'locate_table']


class Event(models.Model):
    PARTY_SIZE = (
        ('1', 'Less than 5'),
        ('2', 'Less than 10'),
        ('3', 'More than 10'),
    )
    # event = models.CharField()
    party = models.CharField(max_length=1, blank=False, choices=PARTY_SIZE)
    event_name = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event_name


# class EventForm(ModelForm):
#     class Meta:
#         model = Event
#         fields = ['party', 'event_name']


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    event = models.ForeignKey(Event,  on_delete=models.CASCADE)
    number_of_people = models.IntegerField(default=1)
    dining_date = models.DateField()
    dining_time = models.TimeField()

    def __str__(self):
        return self.Customer.username

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(Booking, self).save(*args, **kwargs)
        if created:
            Event.objects.create(event=self)
            Table.objects.create(table=self)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    message = models.TextField()


class AboutUs(models.Model):
    subject = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    picture = models.ImageField()

