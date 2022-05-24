from django.shortcuts import render
from .models import category, marca, Product, ProductAtribute
# Create your views here.

def home(request):
    return render(request, 'index.html')

def category_list(request):
    data=category.objects.all().order_by('-id')
    return render(request, 'category_list.html',{'data':data})

def marca_list(request):
    data=marca.objects.all().order_by('-id')
    return render(request, 'marca_list.html',{'data':data})

def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title', 'category__id')
    marcas=Product.objects.distinct().values('marca__title', 'marca__id')
    colors=ProductAtribute.objects.distinct().values('color__title', 'color__id', 'color__color_codigo')
    sizes=ProductAtribute.objects.distinct().values('size__title', 'size__id')
    return render(request, 'product_list.html',
    {
        'data':data,
        'cats':cats,
        'marcas':marcas,
        'colors':colors,
        'sizes':sizes,
        

    }
    )