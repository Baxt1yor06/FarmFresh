from django.db import models
from django.urls import reverse

# Create your models here.

class Index_carousel(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='carousel/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail1", args=[self.slug])
    def __str__(self):
        return self.name

class Carousel_footer(models.Model):
    name =  models.CharField(max_length=200)
    bio = models.TextField()
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detail2", args=[self.slug])

class About(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/')
    skil_name = models.CharField(max_length=200)
    skil_bio = models.TextField()
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail3", args=[self.slug])
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail4", args=[self.slug])
    def __str__(self):
        return self.name


class Features(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    skill_bio = models.TextField()
    img = models.ImageField(upload_to='feature')
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='products/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail6", args=[self.slug])
    def __str__(self):
        return self.name

class Client(models.Model):
    name =  models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='clients/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail7", args=[self.slug])
    def __str__(self):
        return self.name

class Farmers(models.Model):
    name =  models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    img = models.ImageField(upload_to='farmers/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail8", args=[self.slug])
    def __str__(self):
        return self.name

class Posts(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    img = models.ImageField(upload_to='posts/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail9", args=[self.slug])
    def __str__(self):
        return self.name

class Recent_posts(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='recent_posts/')
    def __str__(self):
        return self.name
    

class News(models.Model):
    name =  models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='news/')
    def __str__(self):
        return self.name

class Commets(models.Model):
    name =  models.CharField(max_length=200)
    bio = models.TextField()
    date = models.DateField()
    img = models.ImageField(upload_to='comment/') 
    def __str__(self):
        return self.name 


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self) -> str:
        return self.name  
    

