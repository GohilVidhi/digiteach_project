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


class complaint(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class past_history(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name


class personal_H_O(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name



class PatientCondition(models.Model):
    complaints = models.ManyToManyField(complaint)
    past_history = models.ManyToManyField(past_history)
    personal_H_O = models.ManyToManyField(personal_H_O)
    poller = models.BooleanField(default=False)
    icterus = models.BooleanField(default=False)
    LAP = models.CharField(max_length=250, blank=True)
    clubbing = models.BooleanField(default=False)
    cyanosis = models.BooleanField(default=False)

class FC(models.Model):
    referrer = models.CharField(max_length=250)
    patient_name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.TextField()
    mobile_no = models.BigIntegerField()
    patient_condition = models.OneToOneField(PatientCondition, on_delete=models.CASCADE)
    Opinion = models.TextField()


#==============admin_login==========================
class admin_login(models.Model):
    email=models.EmailField(max_length=255,blank=True,null=True)
    mobile_no = models.BigIntegerField(blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.email

