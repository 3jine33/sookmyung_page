from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    CATEGORY = (
        ('소설', '소설'),
        ('사회/문화', '사회/문화'),
        ('IT', 'IT'),
    )

    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    category=models.CharField(max_length=10, choices=CATEGORY)
    publisher= models.CharField(max_length=255)
    pub_year= models.IntegerField()
    location= models.CharField(max_length=255)
    describe = models.TextField()

    def __str__(self):
        return self.title    


class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    

