from django.shortcuts import render, redirect 
from .models import Brand, Car
from .forms import BrandForm, CarForm


def brands_list(request):
    brands = Brand.objects.all()
    return render(request, 'myapp/brands_list.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, 'myapp/brand_detail.html', {'brand': brand})

def new_brand(request):
    form = BrandForm()
    return render(request, 'myapp/brand_form.html', {'form': form, 'type_of_request': 'new'})

def new_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm()
    return render(request, 'myapp/brand_form.html', {'form': form, 'type_of_request': 'New'})

def edit_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
    return render(request, 'myapp/brand_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    brand.delete()
    return redirect('brands_list')

# def new_car(request):
#     if request.method == "POST":
#         form = CarForm(request.POST)
#         if form.is_valid():
#             car = form.save(commit=False)
#             car.save()
#             return redirect('brand_detail', car_id=car.id)
#     else:
#         form = CarForm()
#     return render(request, 'myapp/car_form.html', {'form': form, 'type_of_request': 'New'})