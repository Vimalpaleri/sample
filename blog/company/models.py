from django.db import models

# Create your models here.
class employee(models.Model):
    DESIGNATION=(
        ('manager','manager com'),
        ('hr','hr com'),
        ('programmer','programmer inc'),
        ('programmer trainee','programmer_trainee com'),
        ('others','others com'),
    )
    
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50,choices=DESIGNATION)
    username=models.CharField(max_length=30,primary_key=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta():
        db_table= "company_employee_details"
class Document(models.Model):
    description = models.CharField(max_length=205,blank=True)
    document = models.FileField(upload_to='document/')
    upload_at = models.DateTimeField(auto_now_add=True)