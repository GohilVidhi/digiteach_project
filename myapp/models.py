from django.db import models

# Create your models here.


class bed(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class ipd(models.Model):
    sr_no=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    datetime_admission=models.CharField(max_length=250)
    bed_data=models.ForeignKey(bed,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=250)
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    address=models.TextField()
    mobile=models.BigIntegerField()
    datetime_discharge=models.CharField(max_length=250,blank=True,null=True)
    dd_note=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.sr_no

class scalp(models.Model):
    sr_no=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    datetime_admission=models.CharField(max_length=250)
    patient_name=models.CharField(max_length=250)
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    address=models.TextField()
    mobile=models.BigIntegerField()
    datetime_discharge=models.CharField(max_length=250,blank=True,null=True)
    fees=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.sr_no








