from django.contrib import admin
from .models import Product, category , color , size , marca, ProductAtribute, Banner

# Register your models here.
admin.site.register(Banner)
admin.site.register(size)


class ColorAdmin(admin.ModelAdmin):
      list_display =('title','color_tag_path')
admin.site.register(color, ColorAdmin)

class MarcaAdmin(admin.ModelAdmin):
      list_display =('title','image_tag_path')
admin.site.register(marca, MarcaAdmin)

class CategoryAdmin(admin.ModelAdmin):
      list_display =('title','image_tag_path')
admin.site.register(category , CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'marca', 'image_tag_path', 'color', 'size', 'status')
    list_editable = ('status',)
admin.site.register(Product, ProductAdmin)

class ProductAtributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size',)
admin.site.register(ProductAtribute, ProductAtributeAdmin)