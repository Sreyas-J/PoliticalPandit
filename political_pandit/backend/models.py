from django.db import models
from django.contrib.auth.models import User

class Keyword(models.Model):
    word=models.TextField(primary_key=True)

    def __str__(self):
        return self.word

class Tweet(models.Model):
    keyword=models.ManyToManyField(Keyword,related_name='tweet')
    like=models.IntegerField(default=0)
    body=models.TextField()

    def __str__(self):
        return self.body

class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE,primary_key=True)
    keywords=models.ManyToManyField(Keyword,related_name='profile')
    points=models.IntegerField(default=0)
    tweets=models.ManyToManyField(Tweet,related_name='profile')
    visited=models.ManyToManyField(Tweet,related_name='profileName')

    def __str__(self):
        return self.user.username

class Party(models.Model):
    name = models.CharField(max_length=100,primary_key=True,unique=True)
    symbol = models.ImageField(null=True)

    def __str__(self):
        return self.name
  
class LokSabhaConstituency(models.Model):
    name = models.CharField(max_length=100,primary_key=True,unique=True)
    const_no = models.IntegerField()
    mp = models.CharField(max_length=200)
    party = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class AssemblyConstituency(models.Model):
    num = models.IntegerField()
    name = models.CharField(primary_key = True, max_length = 200)
    mla = models.CharField(max_length = 200)
    party = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Option(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    query=models.CharField(max_length=100,primary_key=True)
    answer=models.ForeignKey(Option,related_name='question',on_delete=models.SET_NULL,null=True)
    options=models.ManyToManyField(Option,related_name='questions')

    def __str__(self):
        return self.query
    
class Quiz(models.Model):
    questions=models.ManyToManyField(Question,related_name='quiz')
    users=models.ManyToManyField(Profile,related_name='quiz')