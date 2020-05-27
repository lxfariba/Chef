from django.db import models
from account.models import Customer

# Create your models here.


class Food(models.Model):

    CATEGORY_FOR_FOOD_CHOICES = (
        ('PIZ', 'Pizza'),
        ('SAN', 'Sandwich'),
        ('BUR', 'Burger'),
        ('FRI', 'Fried'),
        ('SAL', 'Salad'),
        ('APP', 'Appetizer'),
    )
    RATING_RANG = (
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
    category = models.CharField(max_length=3, choices=CATEGORY_FOR_FOOD_CHOICES, default='Pizza')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    picture_food = models.ImageField(upload_to='food/images')
    rating = models.FloatField(choices=RATING_RANG, null=True, blank=True, default=None)


class FoodQuantity(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return "{} of {}".format(self.quantity, self.food.name)


class Order(models.Model):

    STATUS_ORDER = (
        ('PEN', 'Pending'),
        ('CAN', 'Is Cancelled'),
        ('VER', 'Verified'),
        ('DEL', 'Is Delivered')
    )
    PAYMENT_METHOD_CHOICES = (
        ('CR', 'Credit'),
        ('CA', 'Cash')
    )
    customer = models.ForeignKey(Customer)
    foods = models.ManyToManyField(FoodQuantity)
    status = models.CharField(max_length=3, choices=STATUS_ORDER, blank=True)
    datetime = models.DateTimeField(auto_now=True, blank=True)
    shipping_cost = models.PositiveIntegerField(default=0)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD_CHOICES, blank=True)
    name_delivery = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "%s" % self.Customer.username
