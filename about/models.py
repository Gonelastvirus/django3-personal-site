from django.db import models
# Create your models here.


class About(models.Model):
    title = "About me"
    discription = models.TextField()
    image = models.ImageField(upload_to='portfolio/image/')

    def __str__(self):
        return self.title
