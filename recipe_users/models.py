import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from PIL import Image

class RecipeUser(AbstractUser):
    display_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    # profile_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.display_name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     upload_img = Image.open(self.profile_image.path)
    #     if upload_img.height > 300 or upload_img.width > 300:
    #         output_size = (300,300)
    #         upload_img.thumbnail(output_size)
            # upload_img.save(self.profile_image.path)