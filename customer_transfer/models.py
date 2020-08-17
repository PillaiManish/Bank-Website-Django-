from django.db import models

# Create your models here.
class customer_transfer(models.Model):
    self_userid = models.IntegerField()
    to_userid = models.IntegerField()
    date = models.DateField(auto_now=True)
    to_amount = models.IntegerField()


    def __str__(self):
        return str(self.self_userid)    