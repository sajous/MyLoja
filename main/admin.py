from django.contrib import admin
from .models import Product, category , color , size , marca, ProductAtribute

# Register your models here.

admin.site.register(category)
admin.site.register(marca)
admin.site.register(color)
admin.site.register(size)

class ProductAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'marca', 'color', 'size', 'status')
    list_editable = ('status',)
admin.site.register(Product, ProductAdmin)

class ProductAtributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size',)
admin.site.register(ProductAtribute, ProductAtributeAdmin)