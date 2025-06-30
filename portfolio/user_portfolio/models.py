from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Higher(models.Model):
    college_name=models.CharField(max_length=100)
    start=models.DateField()
    end=models.DateField()
    desc=models.TextField()
    address=models.CharField(max_length=100)
    marks=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.college_name
class Inter(models.Model):
    inter_name=models.CharField(max_length=100)
    start=models.DateField()
    end=models.DateField()
    desc=models.TextField()
    address=models.CharField(max_length=100)
    marks=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.inter_name
class School(models.Model):
    school=models.CharField(max_length=100)
    start=models.DateField()
    end=models.DateField()
    desc=models.TextField(null=True,blank=True)
    address=models.CharField(max_length=100)
    marks=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.school
class Projects(models.Model):
    pname=models.CharField(max_length=100,null=True,blank=True)
    pimage_or_video=models.FileField(upload_to='projects')
    pdesc=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.pname
class Language(models.Model):
    lname=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.lname
class Skills(models.Model):
    ssname=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.ssname
    
class Portfolio(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='userimage/')
    age=models.IntegerField()
    email=models.EmailField(max_length=100,null=True,blank=True)
    address=models.TextField()
    higher_education=models.ForeignKey(Higher,on_delete=models.CASCADE,null=True,blank=True)
    inter=models.ForeignKey(Inter,on_delete=models.CASCADE,null=True,blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    hobbies=models.TextField(null=True,blank=True)
    language=models.ManyToManyField(Language,null=True,blank=True)
    skills=models.ManyToManyField(Skills,null=True,blank=True)
    project=models.ForeignKey(Projects,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    github=models.URLField(null=True,blank=True)
    linkidin=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
