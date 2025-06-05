from django.db import models

# Create your models here.


class bed(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
#==========Specialization=========================
class Specialization(models.Model):
    specialization_name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.specialization_name


#================Doctor================
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100,blank=True,null=True)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE,blank=True,null=True)
    mobile_no = models.BigIntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    date_of_joining=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.doctor_name

class ipd(models.Model):
    sr_no=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    datetime_admission=models.CharField(max_length=250)
    bed_data=models.ForeignKey(bed,on_delete=models.CASCADE)
    doctor_data=models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
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
    bed_data=models.ForeignKey(bed,on_delete=models.CASCADE,blank=True,null=True)
    doctor_data=models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
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
    blood_pressure= models.CharField(max_length=250,blank=True,null=True)
    pulse = models.CharField(max_length=250,blank=True,null=True)
    blood_sugar= models.CharField(max_length=250,blank=True,null=True)
    ECG=models.CharField(max_length=250,blank=True,null=True)
    temperature = models.CharField(max_length=250,blank=True,null=True)
    poller = models.BooleanField(default=False)
    icterus = models.BooleanField(default=False)
    LAP = models.BooleanField(default=False)
    edema_feet = models.BooleanField(default=False)
    clubbing = models.BooleanField(default=False)
    cyanosis = models.BooleanField(default=False)

class FC(models.Model):
    referrer = models.CharField(max_length=250)
    patient_name = models.CharField(max_length=250)
    date=models.CharField(max_length=250,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
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
    type=models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.email


  

#=========Service=========
class Service(models.Model):
    service_name = models.CharField(max_length=100,blank=True,null=True)
    service_price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.service_name

#============OPD=================
class OPD(models.Model):
    sr_no = models.CharField(max_length=250,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    patient_name = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField()
    mobile_no = models.BigIntegerField(blank=True,null=True)
    service_id = models.ManyToManyField(Service)
    doctor_data=models.ForeignKey("Doctor",on_delete=models.CASCADE,blank=True,null=True)
    payment_mode = models.CharField(max_length=250,blank=True,null=True)
    prescription = models.TextField()
    total_amount=models.FloatField(blank=True,null=True)

    def __str__(self):
        return f"{self.patient_name}"



    
class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mobile_no = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    date_of_joining = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.staff_name    


class ad(models.Model):
    file=models.FileField(upload_to="ad")
    


class DC(models.Model):
    sr_no = models.IntegerField()
    date = models.CharField(max_length=255,blank=True,null=True)
    patient_name = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=255,blank=True,null=True)
    address = models.TextField()
    bed_no = models.ForeignKey(bed, on_delete=models.CASCADE)
    date_of_admission = models.CharField(max_length=255,blank=True,null=True)
    date_of_discharge = models.CharField(max_length=255,blank=True,null=True)
    type_of_discharge = models.CharField(max_length=255,blank=True,null=True)
    diagnosis = models.CharField(max_length=255,blank=True,null=True)
    clinical_notes = models.CharField(max_length=255,blank=True,null=True)
    investigation = models.CharField(max_length=255,blank=True,null=True)
    treatment_given = models.CharField(max_length=255,blank=True,null=True)
    # check_up_details = models.JSONField(default=dict)  

    def __str__(self):
        return f"Patient {self.sr_no} - Bed {self.bed_no}"
