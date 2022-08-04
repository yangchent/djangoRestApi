from django.db import models
import pathlib
import uuid


# def restaurant_image_upload_handler(instance, filename):
#     fpath = pathlib.path(filename)
#     new_fname = str(uuid.uuid1())
#     return f"images/{new_fname}{fpath.suffix}"

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=64, default="Paris")
    Zip_code = models.CharField(max_length=5, default="75001")
    phone = models.CharField(max_length=15, default="0000000000")
    deliveroo = models.CharField(max_length=150, blank=True)
    uber = models.CharField(max_length=150, blank=True)
    link = models.CharField(max_length=150, blank=True)
    fork = models.CharField(max_length=150, blank=True)
    image= models.ImageField(upload_to='images', blank=True)
    image_one= models.ImageField(upload_to='images', blank=True)
    image_two= models.ImageField(upload_to='images', blank=True)
    image_three= models.ImageField(upload_to='images', blank=True)
    image_four= models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name

class Boutique(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150,default="Boutique")
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=64, default="Paris")
    Zip_code = models.CharField(max_length=5, default="75001")
    phone = models.CharField(max_length=15)
    link = models.CharField(max_length=200, blank=True)
    image= models.ImageField(upload_to='images', blank=True)
    image_one= models.ImageField(upload_to='images', blank=True)
    image_two= models.ImageField(upload_to='images', blank=True)
    image_three= models.ImageField(upload_to='images', blank=True)
    image_four= models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name

class Ngo(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=64, default="Paris")
    Zip_code = models.CharField(max_length=5, default="75001")
    phone = models.CharField(max_length=15)
    link = models.CharField(max_length=200, blank=True)
    type_of_ngo = models.CharField(max_length=200, default="ONG")
    image= models.ImageField(upload_to='images', blank=True)
    image_one= models.ImageField(upload_to='images', blank=True)
    image_two= models.ImageField(upload_to='images', blank=True)
    image_three= models.ImageField(upload_to='images', blank=True)
    image_four= models.ImageField(upload_to='images', blank=True)

# class Contact(models.Model):
#     firstname = models.CharField(max_length=50 )
#     lastname = models.CharField(max_length=50, )
#     email = models.CharField(max_length=80,  blank=False )
#     message = models.TextField(max_length=500,  blank=False )

    def __str__(self):
        return self.name