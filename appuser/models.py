from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class AppUser(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    emailaddress = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.firstname