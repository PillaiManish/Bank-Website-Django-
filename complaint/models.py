from django.db import models

# Create your models here.
class customer_complaints(models.Model):
    userid = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=20)
    complaint = models.CharField(max_length=150)
    return_date = models.DateField(null=True,blank=True)
    return_message = models.CharField(null=True,blank=True,max_length=500)

    def __str__(self):
        return str(self.userid)