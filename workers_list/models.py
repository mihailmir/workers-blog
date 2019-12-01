from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Workers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField()
    image = models.ImageField(default='workers_list/photos/default_user.jpg', upload_to='workers_list/photos',
                              verbose_name='Фото сотрудника')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Workers.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.workers.save()
