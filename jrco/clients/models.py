from django.db import models

# Create your models here.
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Client(TimeStampMixin):
    image = models.ImageField(upload_to='clients/')
    name = models.CharField(max_length=50)
    desc = models.TextField()


    def __str__(self):
        return str(self.name)