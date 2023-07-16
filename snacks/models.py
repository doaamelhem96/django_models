from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack (models.Model):
    name=models.CharField(max_length=46,help_text='enter name')
    rank=models.IntegerField()
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    description = models.TextField(blank=True)

    def __string__ (self):
        return self.name

