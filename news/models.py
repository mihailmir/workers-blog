from django.db import models

# Create your models here.


class News(models.Model):
    image = models.ImageField(upload_to='news/image', verbose_name='Фото новости')
    text = models.TextField(verbose_name='Текс новости')
