from django.db import models

# Create your models here.
class userr(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta():
        db_table= "user_reg_user"
