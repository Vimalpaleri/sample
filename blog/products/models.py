from django.db import models

# Create your models here.
class products(models.Model):
    BRANDS=(
        ('apple','apple inc'),
        ('microsoft','microsoft inc'),
        ('google','google inc'),
    )
    
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=50,choices=BRANDS)
    quantity=models.IntegerField()
    price=models.FloatField()
    def __str__(self):
        return self.name
    class Meta():
        db_table= "products_custom_products"
class buyers(models.Model):
    name=models.CharField(max_length=50)
    productid=models.IntegerField()
    email=models.EmailField()
    price=models.FloatField()
    warranty=models.IntegerField()
    class Meta():
        db_table="products_buyers_products"