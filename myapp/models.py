from django.db import models
from django_mysql.models import ListTextField

# Create your models here.


class Designation(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
  

class School(models.Model):
    school_name=models.CharField(max_length=250,blank=True,null=True)
    school_email=models.EmailField(max_length=250,blank=True,null=True)
    school_address=models.TextField(blank=True,null=True)
    contact_person_name=models.CharField(max_length=250,blank=True,null=True)
    contact_number=models.IntegerField(blank=True,null=True)
    designation_data=models.ForeignKey(Designation,on_delete=models.CASCADE)
    address_line_1=models.TextField(blank=True,null=True)
    address_line_2=models.TextField(blank=True,null=True)
    landmark=models.CharField(max_length=250,blank=True,null=True)
    city=models.CharField(max_length=250,blank=True,null=True)
    district=models.CharField(max_length=250,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.school_name
  
  
  
class Job(models.Model):
    school_data = models.ForeignKey(School,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_type = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    experience_required = models.CharField(max_length=50)
    qualification = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=50)
    posted_date = models.CharField(max_length=255)
    last_date_to_apply = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.job_title
    
    
    
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20,blank=True, null=True)
    dob = models.CharField(max_length=255,blank=True, null=True)
    gender = models.CharField(max_length=10,blank=True, null=True)
    address = models.JSONField(blank=True, null=True,default=dict)
    qualification = models.CharField(max_length=255,blank=True, null=True)
    experience = models.CharField(max_length=50,blank=True, null=True)
    subjects = ListTextField(default=[],base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    preferred_classes = ListTextField(default=[],base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    resume_url = models.FileField(upload_to="resumes",blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_images",blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)

    expected_salary = models.CharField(max_length=50,blank=True, null=True)
    availability = models.CharField(max_length=50,blank=True, null=True)
    skills = ListTextField(default=[],base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    languages_known = ListTextField(default=[],base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,blank=True, null=True)

    # def __str__(self):
    #     return self.full_name
    
    
class Job_Apply(models.Model):
    job_data = models.ForeignKey(Job, on_delete=models.CASCADE,blank=True, null=True)
    teacher_data = models.ForeignKey(Teacher, on_delete=models.CASCADE,blank=True, null=True)
    applied_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    status = models.CharField(max_length=255,blank=True, null=True)
