
from rest_framework import serializers
from .models import *
class bed_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=bed
        fields ='__all__'
        

    def create(self, validated_data):
        return bed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance        

class ipd_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    bed_data = serializers.SlugRelatedField(slug_field='id', queryset=bed.objects.all(), required=True)
    doctor_data = serializers.SlugRelatedField(slug_field='id', queryset=Doctor.objects.all(), required=True)
    sr_no = serializers.CharField(max_length=250)
    date = serializers.CharField(max_length=250)
    datetime_admission = serializers.CharField(max_length=250)
    patient_name = serializers.CharField(max_length=250)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=250)
    address = serializers.CharField()
    mobile = serializers.IntegerField()
    datetime_discharge=serializers.CharField(max_length=250, required=False)
    dd_note=serializers.CharField(max_length=250, required=False)
   

    class Meta:
        models=ipd
        fields ='__all__'
        

    def create(self, validated_data):
        return ipd.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sr_no = validated_data.get('sr_no', instance.sr_no)
        instance.date = validated_data.get('date', instance.date)
        instance.datetime_admission = validated_data.get('datetime_admission', instance.datetime_admission)
        instance.bed_data = validated_data.get('bed_data', instance.bed_data)
        instance.doctor_data = validated_data.get('doctor_data', instance.doctor_data)
        instance.patient_name = validated_data.get('patient_name', instance.patient_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.address = validated_data.get('address', instance.address)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.datetime_discharge = validated_data.get('datetime_discharge', instance.datetime_discharge)
        instance.dd_note = validated_data.get('dd_note', instance.dd_note)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["bed_data"] = bed_serializers(instance.bed_data).data  
        representation["doctor_data"] = DoctorSerializer(instance.doctor_data).data 
        return representation        



class scalp_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    bed_data = serializers.SlugRelatedField(slug_field='id', queryset=bed.objects.all(), required=True)
    doctor_data = serializers.SlugRelatedField(slug_field='id', queryset=Doctor.objects.all(), required=True)
    sr_no = serializers.CharField(max_length=250)
    date = serializers.CharField(max_length=250)
    datetime_admission = serializers.CharField(max_length=250)
    patient_name = serializers.CharField(max_length=250)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=250)
    address = serializers.CharField()
    mobile = serializers.IntegerField()
    datetime_discharge=serializers.CharField(max_length=250, required=False)
    fees=serializers.IntegerField(default=0)
      

    class Meta:
        models=scalp
        fields ='__all__'
        

    def create(self, validated_data):
        return scalp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sr_no = validated_data.get('sr_no', instance.sr_no)
        instance.date = validated_data.get('date', instance.date)
        instance.datetime_admission = validated_data.get('datetime_admission', instance.datetime_admission)
        instance.patient_name = validated_data.get('patient_name', instance.patient_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.address = validated_data.get('address', instance.address)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.datetime_discharge = validated_data.get('datetime_discharge', instance.datetime_discharge)
        instance.fees = validated_data.get('fees', instance.fees)
        instance.bed_data = validated_data.get('bed_data', instance.bed_data)
        instance.doctor_data = validated_data.get('doctor_data', instance.doctor_data)
        instance.save()
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["bed_data"] = bed_serializers(instance.bed_data).data  
        representation["doctor_data"] = DoctorSerializer(instance.doctor_data).data 
        return representation   







class complaint_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=complaint
        fields ='__all__'
        

    def create(self, validated_data):
        return complaint.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance     
    


class past_history_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=past_history
        fields ='__all__'
        

    def create(self, validated_data):
        return past_history.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance     
    
    
class personal_H_O_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=personal_H_O
        fields ='__all__'
        

    def create(self, validated_data):
        return personal_H_O.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance     


class PatientConditionSerializer(serializers.Serializer):
    complaints = serializers.PrimaryKeyRelatedField(queryset=complaint.objects.all(), many=True)
    past_history = serializers.PrimaryKeyRelatedField(queryset=past_history.objects.all(), many=True)
    personal_H_O = serializers.PrimaryKeyRelatedField(queryset=personal_H_O.objects.all(), many=True)
    blood_pressure= serializers.CharField(required=False,allow_null=True, allow_blank=True)
    pulse = serializers.CharField(required=False,allow_null=True, allow_blank=True)
    blood_sugar= serializers.CharField(required=False,allow_null=True, allow_blank=True)
    ECG=serializers.CharField(required=False,allow_null=True, allow_blank=True)
    temperature = serializers.CharField(required=False,allow_null=True, allow_blank=True)
    poller = serializers.BooleanField(required=False)
    icterus = serializers.BooleanField(required=False)
    LAP = serializers.BooleanField(required=False)
    edema_feet = serializers.BooleanField(required=False)
    clubbing = serializers.BooleanField(required=False)
    cyanosis = serializers.BooleanField(required=False)
    class Meta:
        model = PatientCondition
        fields = [
            'complaints', 'past_history', 'personal_H_O',
            'poller', 'icterus', 'LAP', 'clubbing', 'cyanosis','edema_feet'
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["complaints"] = complaint_serializers(instance.complaints,many=True).data  
        representation["past_history"] = past_history_serializers(instance.past_history,many=True).data  
        representation["personal_H_O"] = personal_H_O_serializers(instance.personal_H_O,many=True).data  
        for field in ['blood_pressure', 'pulse', 'blood_sugar', 'ECG', 'temperature']:
            if representation.get(field) is None:
                representation[field] = ""
        return representation     

class FCSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    patient_condition = PatientConditionSerializer()

    class Meta:
        model = FC
        fields = "__all__"

    def create(self, validated_data):
        condition_data = validated_data.pop('patient_condition')
      
        complaints = condition_data.pop('complaints')
        past_history = condition_data.pop('past_history')
        personal_H_O = condition_data.pop('personal_H_O')

        patient_condition = PatientCondition.objects.create(**condition_data)
        patient_condition.complaints.set(complaints)
        patient_condition.past_history.set(past_history)
        patient_condition.personal_H_O.set(personal_H_O)
        patient_condition.save()

        fc_instance = FC.objects.create(patient_condition=patient_condition, **validated_data)
        return fc_instance
    def update(self, instance, validated_data):
        # Extract patient_condition data from validated data
        condition_data = validated_data.pop('patient_condition', {})

        # Handle the many-to-many fields (complaints, past_history, personal_H_O)
        complaints = condition_data.pop('complaints', [])
        past_history = condition_data.pop('past_history', [])
        personal_H_O = condition_data.pop('personal_H_O', [])

        # Update the PatientCondition instance
        patient_condition = instance.patient_condition
        for attr, value in condition_data.items():
            setattr(patient_condition, attr, value)

        # Set the many-to-many relationships for the updated PatientCondition instance
        if complaints:
            patient_condition.complaints.set(complaints)
        if past_history:
            patient_condition.past_history.set(past_history)
        if personal_H_O:
            patient_condition.personal_H_O.set(personal_H_O)

        patient_condition.save()

        # Update other fields in FC model
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance





#-------------admin_login_serializers ----------------
import pytz
class admin_login_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=50,required=False)
    mobile_no = serializers.IntegerField(required=False)
    password=serializers.CharField(max_length=50,required=True)
    type=serializers.CharField(max_length=50,required=False)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        models=admin_login
        fields ='__all__'
        exclude = ('id',)
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    # def create(self, validated_data):
    #     return admin_login.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.email=validated_data.get('email',instance.email)
    #     instance.password=validated_data.get('password',instance.password)

    #     instance.save()
    #     return instance





   
#=====================ServiceSerializer==========
class ServiceSerializer(serializers.Serializer):
    service_name=serializers.CharField(max_length=250,required=True)
    service_price = serializers.FloatField(required=True )
    class Meta:
        model = Service
        fields = '__all__'

    def create(self, validated_data):
        return Service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service_name = validated_data.get('service_name', instance.service_name)
        instance.service_price = validated_data.get('service_price', instance.service_price)
        instance.save()
        return instance

#===================OPDSerializer===========================
class OPDSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    service_id = serializers.SlugRelatedField(slug_field='id', queryset=Service.objects.all(),many=True, required=True)
    doctor_data = serializers.SlugRelatedField(slug_field='id', queryset=Doctor.objects.all(), required=True)
    sr_no = serializers.CharField(max_length=100,required=False)
    patient_name = serializers.CharField(max_length=100,required=False)
    age = serializers.IntegerField(required=False)
    mobile_no = serializers.IntegerField(required=False)
    gender = serializers.CharField(max_length=100,required=False)
    address = serializers.CharField(max_length=250,required=False)
    payment_mode = serializers.CharField(max_length=250,required=False)
    prescription = serializers.CharField(max_length=250,required=False)
    date = serializers.SerializerMethodField()
    total_amount = serializers.FloatField(required=False)


    class Meta:
        model = OPD
        fields = '__all__'
        read_only_fields = ['date']
    def get_date(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.date.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')        
        
    def create(self, validated_data):
        service_data = validated_data.pop('service_id', [])
        opd_instance = OPD.objects.create(**validated_data)
        opd_instance.service_id.set(service_data)
        return opd_instance

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.sr_no = validated_data.get('sr_no', instance.sr_no)
        instance.patient_name = validated_data.get('patient_name', instance.patient_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.address = validated_data.get('address', instance.address)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.payment_mode = validated_data.get('payment_mode', instance.payment_mode)
        instance.prescription = validated_data.get('prescription', instance.prescription)
        instance.doctor_data = validated_data.get('doctor_data', instance.doctor_data)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        service_data = validated_data.pop('service_id', None)
        if service_data is not None:
            instance.service_id.set(service_data)
        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["service_id"] = ServiceSerializer(instance.service_id,many=True).data  
        representation["doctor_data"] = DoctorSerializer(instance.doctor_data).data  
        return representation           
    
#====================SpecializationSerializer=====================
class SpecializationSerializer(serializers.Serializer):
    specialization_name = serializers.CharField(max_length=100,required=False)
    class Meta:
        model = Specialization
        fields = '__all__'
        
    def create(self, validated_data):
        return Specialization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.specialization_name = validated_data.get('specialization_name', instance.specialization_name)
        instance.save()
        return instance        

#=================DoctorSerializer==================================
class DoctorSerializer(serializers.Serializer):
    doctor_name = serializers.CharField(max_length=100,required=False)
    specialization_id = serializers.SlugRelatedField(slug_field='id', queryset=Specialization.objects.all(), required=True)
    address = serializers.CharField(max_length=250,required=False)
    mobile_no = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)
    date_of_joining = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['date_of_joining']
    def get_date_of_joining(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.date_of_joining.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.doctor_name = validated_data.get('doctor_name', instance.doctor_name)
        instance.specialization_id = validated_data.get('specialization_id', instance.specialization_id)
        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["specialization_id"] = SpecializationSerializer(instance.specialization_id).data  
        return representation
    


#===================StaffSerializer===========================
class StaffSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    staff_name = serializers.CharField(max_length=100, required=True)
    department = serializers.CharField(max_length=100, required=True)
    mobile_no = serializers.CharField(max_length=15, required=True)
    email = serializers.EmailField(required=True)
    address = serializers.CharField(required=True)
    date_of_joining = serializers.SerializerMethodField()


    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ['date_of_joining']
    def get_date_of_joining(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.date_of_joining.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')        
        
    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.staff_name = validated_data.get('staff_name', instance.staff_name)
        instance.department = validated_data.get('department', instance.department)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.date_of_joining = validated_data.get('date_of_joining', instance.date_of_joining)
        instance.save()
        return instance



class ad_serializers(serializers.ModelSerializer):
    class Meta:
        model = ad
        fields = ['id', 'file']
    
    def create(self, validated_data):
        return ad.objects.create(**validated_data)
         

    def update(self, instance, validated_data):
        # Handle file upload in the update method
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance
    



#=========================================================
class DCSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    
    sr_no = serializers.IntegerField()
    date = serializers.CharField(required=True)
    patient_name = serializers.CharField(max_length=100,required=False)
    age = serializers.IntegerField()
    gender = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
   
    date_of_admission = serializers.CharField(required=True)
    date_of_discharge = serializers.CharField(required=True)
    type_of_discharge = serializers.CharField(required=True)
    diagnosis = serializers.CharField(required=True)
    clinical_notes = serializers.CharField(required=True)
    investigation = serializers.CharField(required=True)
    treatment_given = serializers.CharField(required=True)
    bed_no = serializers.SlugRelatedField(slug_field='id', queryset=bed.objects.all(), required=True)
    # check_up_details = serializers.JSONField(required=False) 
    # REQUIRED_CHECKUP_KEYS = {'gc', 'bp', 'pr', 'rs', 'cvs', 'cns'}
    class Meta:
        model = DC
        fields = '__all__'
        
        
    # def validate_check_up_details(self, value):
    #     if not isinstance(value, dict):
    #         raise serializers.ValidationError("check_up_details must be a dictionary.")
        
    #     keys = set(value.keys())

    #     if not keys.issubset(self.REQUIRED_CHECKUP_KEYS):
    #         invalid_keys = keys - self.REQUIRED_CHECKUP_KEYS
    #         raise serializers.ValidationError(f"Invalid keys in check_up_details: {', '.join(invalid_keys)}")

    #     return value
    def create(self, validated_data):
        return DC.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.sr_no = validated_data.get('sr_no', instance.sr_no)
        instance.date = validated_data.get('date', instance.date)
        instance.patient_name = validated_data.get('patient_name', instance.patient_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.address = validated_data.get('address', instance.address)
        instance.bed_no = validated_data.get('bed_no', instance.bed_no)
        instance.date_of_admission = validated_data.get('date_of_admission', instance.date_of_admission)
        instance.date_of_discharge = validated_data.get('date_of_discharge', instance.date_of_discharge)
        instance.type_of_discharge = validated_data.get('type_of_discharge', instance.type_of_discharge)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.clinical_notes = validated_data.get('clinical_notes', instance.clinical_notes)
         
        instance.treatment_given = validated_data.get('treatment_given', instance.treatment_given)
        # new_checkup = validated_data.get('check_up_details')
        # if new_checkup:
        #     existing_checkup = instance.check_up_details or {}
        #     existing_checkup.update(new_checkup)
        #     instance.check_up_details = existing_checkup 

        instance.save()
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["bed_no"] = bed_serializers(instance.bed_no).data  
        return representation  