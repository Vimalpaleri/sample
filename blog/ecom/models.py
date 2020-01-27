from django.db import models
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='def.jpg')


    class Meta():
        db_table= "ecom_category"
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
class prod(models.Model):
    categorys = models.ForeignKey('category',on_delete=models.CASCADE)   
    pname=models.CharField(max_length=50)
    catogeryy=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=50)
    class Meta():
        db_table="ecom_product"
    def __unicode__(self):
        return self.name
    

