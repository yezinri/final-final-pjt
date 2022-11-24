from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings # 11.24 민혁 추가

# Create your models here.
# 11.24 special thx to David.U
def profile_image_path(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'
    
class User(AbstractUser):
    pass


# 11.24 민혁 추가
class ProfileImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # profile_image = models.ImageField(blank=True)
    profile_image = models.ImageField(blank=True, upload_to=profile_image_path)