from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads')
    description = models.CharField(max_length=50, verbose_name='Опис')

    def __str__(self):
        return self.description



