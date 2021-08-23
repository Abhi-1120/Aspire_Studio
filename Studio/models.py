from django.db import models


class Photo(models.Model):
    photo_id = models.AutoField
    title = models.CharField(max_length=20)
    images = models.ImageField(upload_to="Studio/images")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
