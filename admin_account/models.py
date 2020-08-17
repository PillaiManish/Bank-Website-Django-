from django.db import models

# Create your models here.
class account_balance(models.Model):
    #  user id should be int here
    userid = models.IntegerField() # change still it is in char field
    balance = models.IntegerField(default=100)

    def __str__(self):
        return str(self.userid)