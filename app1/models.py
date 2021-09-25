from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
names =[
('12','aparna'),
('13','manu'),
('14','ganesh'),
('15','ajay'),
('16','anusha')
]

def validate_delhi(value):
    if "delhi" in value:
        return value
    else:
        raise ValidationError("delhi should be the place")

def  comment (value):
    if "good" in value:
      return value
    elif "verygood" in value:
      return value
    elif "excellent" in value:
      return value
    else:
        raise ValidationError("please give correct comment")
class Post(models.Model):
   name=models.CharField(max_length=100,choices=names)
   adress=models.CharField(max_length=100)
   present=models.BooleanField(null=True)
   num=models.IntegerField(null=True)
   phnum=models.BigIntegerField(null=True)
   created_date=models.DateTimeField(auto_now_add=True,null=True)
   student_updated=models.DateTimeField(auto_now=True,null=True)
   student_date=models.DateTimeField(default=timezone.now())
   rating=models.TextField(null=True,blank=True,help_text="plz fill rating starting from 5 star ")
   email=models.EmailField(default="mi@gmail.com")
   Profile_pic=models.ImageField(upload_to="images/%y/%m/%d",null=True)
   Resume=models.FileField(upload_to="userfiles/%y/%m/%d",null=True)
   #adress1=models.CharField(max_length=250,validators=[validate_delhi])
   comment=models.TextField(validators=[comment],null=True)
   def save(self,*args,**kwargs):
       if not self.rating:
              self.rating="fivestar"
       super(Post,self).save(*args,**kwargs)
   def __str__(self):
       return self.name

class employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_a=models.CharField(max_length=100)
    def __str__(self):
        return self.emp_name
class salary(models.Model):
    employee=models.OneToOneField(employee,on_delete=models.CASCADE)
    salary=models.BigIntegerField()

class author(models.Model):
    author_name=models.CharField(max_length=200)
    author_language=models.CharField(max_length=200)
    def __str__(self):
        return self.author_name
class novel(models.Model):
    novel=models.ForeignKey(author,on_delete=models.CASCADE)
    novel_name=models.CharField(max_length=200)
    def __str__(self):
        return self.novel_name

class Member(models.Model):
    member_name=models.CharField(max_length=200)
    def __str__(self):
        return self.member_name
class club(models.Model):
    member=models.ManyToManyField(Member)
    club_name=models.CharField(max_length=200)
    def __str__(self):
        return self.club_name




#Crdefe your views here.
# Create your models here.
