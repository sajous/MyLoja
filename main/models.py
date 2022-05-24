
from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Banner(models.Model):
    img = models.CharField(max_length= 255)
    alt_text = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = '1. Banners'
    def __str__(self):
        return self.alt_text

class category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="cat_imgs/")
    class Meta:
        verbose_name_plural = '2. Categorias'
    
    def image_tag_path(self):
        return mark_safe('<img src="%s" witdh="90" height="90" />' %(self.img.url))

    def __str__(self):
        return self.title

class marca(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="cat_imgs/")
    class Meta:
        verbose_name_plural = '3. Marcas'
    
    def image_tag_path(self):
        return mark_safe('<img src="%s" witdh="90" height="90" />' %(self.img.url))
    
    def __str__(self):
        return self.title
        
class color(models.Model):
    title = models.CharField(max_length=255)
    color_codigo = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = '4. Cores'
        
    def color_tag_path(self):
        return mark_safe('<div style=" width:30px; height:30px; background:%s;"></div>' %(self.color_codigo))
        

    def __str__(self):
        return self.title

class size(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = '5. Tamanhos'
    
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length=255)
    detail = models.TextField()
    specs = models.TextField()
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    color  = models.ForeignKey(color, on_delete=models.CASCADE)
    size = models.ForeignKey(size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = '6. Produtos'
    
    def image_tag_path(self):
        return mark_safe('<img src="%s" witdh="90" height="90" />' %(self.img.url))

    def __str__(self):
        return self.title

class ProductAtribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(color, on_delete=models.CASCADE)
    size = models.ForeignKey(size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    class Meta:
        verbose_name_plural = '7. Atributos dos Produtos'


