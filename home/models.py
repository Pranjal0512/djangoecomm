from django.db import models

# Create your models here.
class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)


    def __str__(self):
        return self.title

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500,blank = True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class  Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class  Testimonial(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    post = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
class Service(models.Model):
    title= models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.name
