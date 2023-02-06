from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def  __str__(self):
        return self.name + ' ' + self.surname