from django.db import models
from django.utils import timezone

from recipe_users.models import RecipeUser

class Food(models.Model):
    food_title = models.CharField(max_length=30)
    ingredients = models.TextField()
    directions = models.TextField()
    food_date = models.DateTimeField(default=timezone.now)
    food_author = models.ForeignKey(RecipeUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_title


