from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=64)
    registered_dttm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
