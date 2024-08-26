from django.db import models


class student(models.Model):

    firstName = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    birthday = models.DateField()
    sex = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
    emailAdd = models.EmailField(unique = True)
    studentId = models.IntegerField(unique = True)
    course = models.CharField(max_length = 100)
    yearLevel = models.IntegerField()
    status = models.CharField(max_length = 20)
    image = models.ImageField()
    
    
    def __str__(self):
        return f'{self.firstName} {self.lastname}'
    
    