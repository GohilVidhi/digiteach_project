from django.db import models

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
  
  