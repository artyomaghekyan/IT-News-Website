from django.db import models

# Create your models here.

class News(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='')
    title = models.CharField(max_length=200)
    description = models.TextField()
    creaed = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title#C:\Users\HP\Desktop\news\media\media\images\