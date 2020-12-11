from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('brand_name', 'brand_country')

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('car_name',)