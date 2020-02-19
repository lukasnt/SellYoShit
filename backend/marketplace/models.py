from django.db import models


# Create your models here.
class SaleItem(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
