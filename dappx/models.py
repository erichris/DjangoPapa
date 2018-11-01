from django.db import models
from django.contrib.auth.models import User
import datetime
from phone_field import PhoneField
from pipenv.vendor.cerberus.errors import MAX_LENGTH
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.TextField(blank=True)
    pay = models.BooleanField(default=False);
    pay_expire = models.DateField(default=datetime.date.today);
    token = models.TextField(blank=True);
    #portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
      return self.user.username
