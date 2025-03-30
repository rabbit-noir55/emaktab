from django.db import models

# Create your models here.
class Users(models.Model):
  login=models.CharField(max_length=150,unique=True)
  password=models.CharField(max_length=150)
  limit=models.IntegerField(null=True,blank=True, default="30")
  is_bloked=models.BooleanField(default=False)
  def __str__(self):
     return self.login