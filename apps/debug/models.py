from django.db import models

# Create your models here.
class Log(models.Model):
    text = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
