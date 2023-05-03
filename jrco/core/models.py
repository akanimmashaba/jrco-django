from django.db import models

# Create your models here.


class Company(models.Model):
    description = models.TextField()
    comp_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    bee_no = models.CharField(max_length=100)
    bbbee_level = models.IntegerField(default=1)
    

    def __str__(self):
        return str(self.comp_name)