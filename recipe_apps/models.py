import os
from django.db import models
from django.utils import timezone
from PIL import Image

from recipe_users.models import RecipeUser

class Food(models.Model):
    food_title = models.CharField(max_length=30)
    ingredients = models.TextField()
    directions = models.TextField()
    food_date = models.DateTimeField(default=timezone.now)
    food_image = models.ImageField(upload_to='media/')
    food_author = models.ForeignKey(RecipeUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        upload_img = Image.open(self.food_image.path)
        if upload_img.height > 300 or upload_img.width > 300:
            output_size = (300,300)
            upload_img.thumbnail(output_size)
            upload_img.save(self.food_image.path)


