from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(("Ad-Soyad"), max_length=100, blank=True, null=True)
    phone = models.CharField(("Telefon"), max_length=50, blank=True, null=True)
    email = models.CharField(("Email"), max_length=100, blank=True, null=True)
    subject = models.CharField(("Konu"), max_length=120, blank=True, null=True)
    message = models.TextField(("Mesaj"), blank=True, null=True)
    
    def __str__(self):
        return self.fullname
    
class Project(models.Model):
    title = models.CharField(("Başlığı"), max_length=120)
    description = models.TextField(("Açıklaması"))
    image = models.ImageField(("Fotoğrafı"))
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    fullname = models.CharField(("Ad-Soyad"), max_length=100, blank=True, null=True)
    company = models.CharField(("Şirket"), max_length=100, blank=True, null=True)
    message = models.TextField(("Mesaj"), blank=True, null=True)
    
    def __str__(self):
        return self.company
    
class Team(models.Model):
    fullname = models.CharField(("Ad-Soyad"), max_length=100, blank=True, null=True)
    image = models.ImageField(("Fotoğrafı"), blank=True, null=True)
    job = models.CharField(("Meslek"), max_length=100, blank=True, null=True)
    twitter_link = models.CharField(("Twitter Link"), max_length=100, blank=True, null=True)
    facebook_link = models.CharField(("Facebook Link"), max_length=100, blank=True, null=True)
    instagram_link = models.CharField(("İnstagram Link"), max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(("Linked-in Link"), max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.fullname