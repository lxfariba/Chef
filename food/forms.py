from django import forms


class FoodDetailForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.CharField(max_length=5)
    rating = forms.CharField(max_length=3)
