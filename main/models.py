
from django.db import models

# Create your models here.

class Banner(models.Model):
    img = models.CharField(max_length= 255)
    alt_text = models.CharField(max_length=255)


class category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title

class marca(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="cat_imgs/")
    
    def __str__(self):
        return self.title
        
class color(models.Model):
    title = models.CharField(max_length=255)
    color_codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class size(models.Model):
    title = models.CharField(max_length=100)
    
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
    color = models.ForeignKey(color, on_delete=models.CASCADE)
    size = models.ForeignKey(size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ProductAtribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(color, on_delete=models.CASCADE)
    size = models.ForeignKey(size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()


