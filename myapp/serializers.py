
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
    datetime_admission  = serializers.CharField(max_length=250)
    patient_name = serializers.CharField(max_length=250)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=250)
    address = serializers.CharField()
    mobile = serializers.IntegerField()
    datetime_discharge=serializers.CharField(max_length=250, required=False)
    dd_note=serializers.CharField(max_length=250, required=False)

    payment_details = serializers.JSONField(required=False) 
    past_historys = serializers.JSONField(required=False) 
    daily_chief_complaints = serializers.JSONField(required=False) 
    systemetic_examination = serializers.JSONField(required=False) 
    general_examination = serializers.JSONField(required=False) 
    daily_examination = serializers.JSONField(required=False) 
    given_medicine = serializers.JSONField(required=False) 
    daily_given_treatment = serializers.JSONField(required=False) 
    referred_by = serializers.CharField(max_length=250, required=False)
    date_of_refer = serializers.CharField(max_length=250, required=False)
    advice  = serializers.CharField(max_length=1000)
    discharge_condition  = serializers.CharField(max_length=1000)
   

    class Meta:
        models=ipd
        fields ='__all__'

    def validate_payment_details(self, value):
       
        if value is None:
            raise serializers.ValidationError("Staff ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("staff_data")
            if cid is None:
                raise serializers.ValidationError("Staff ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for staff ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            Staff.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Staff(s) with ID(s) {missing_ids} not found in the staff master list."
            )

        return value  

    def validate_past_historys(self, value):
       
        if value is None:
            raise serializers.ValidationError("Past History ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("past_history_data")
            if cid is None:
                raise serializers.ValidationError("Past History ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for Past History ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            past_history.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Past History (s) with ID(s) {missing_ids} not found in the Past History master list."
            )

        return value 

    def validate_daily_chief_complaints(self, value):
        if not value:
            raise serializers.ValidationError("Chief complaints list cannot be empty.")

        complaint_ids = []
        for item in value:
            chief_complaints = item.get("chief_complaints", [])
            for complaints in chief_complaints:
                cid = complaints.get("complaints_data")
                print(cid)  
                if cid is None:
                    raise serializers.ValidationError("complaints_data is required for each complaint.")
                if not isinstance(cid, int):
                    raise serializers.ValidationError(f"Invalid complaints_data '{cid}': must be an integer.")
                complaint_ids.append(cid)

        # Validate all IDs exist
        existing_ids = complaint.objects.filter(id__in=complaint_ids).values_list('id', flat=True)
        missing_ids = [cid for cid in complaint_ids if cid not in existing_ids]

        if missing_ids:
            raise serializers.ValidationError(
                f"complaints_data ID(s) not found: {missing_ids}"
            )

        return value
    
    def validate_systemetic_examination(self, value):
       
        if value is None:
            raise serializers.ValidationError("Staff ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("staff_data")
            if cid is None:
                raise serializers.ValidationError("Staff ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for staff ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            Staff.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Staff(s) with ID(s) {missing_ids} not found in the staff master list."
            )

        return value  

    def validate_general_examination(self, value):
       
        if value is None:
            raise serializers.ValidationError("Staff ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("staff_data")
            if cid is None:
                raise serializers.ValidationError("Staff ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for staff ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            Staff.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Staff(s) with ID(s) {missing_ids} not found in the staff master list."
            )

        return value 
    
    def validate_daily_examination(self, value):
       
        if value is None:
            raise serializers.ValidationError("Staff ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("staff_data")
            if cid is None:
                raise serializers.ValidationError("Staff ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for staff ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            Staff.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Staff(s) with ID(s) {missing_ids} not found in the staff master list."
            )

        return value  

    def validate_given_medicine(self, value):
       
        if value is None:
            raise serializers.ValidationError("Medicine ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("medicine_data")
            if cid is None:
                raise serializers.ValidationError("Medicine ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for Medicine ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            medicine.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Medicine(s) with ID(s) {missing_ids} not found in the Medicine list."
            )

        return value     
    
    def validate_daily_given_treatment(self, value):
        if not value:
            raise serializers.ValidationError("daily_given_treatment cannot be empty.")

        staff_ids = []
        medicine_ids = []

        for item in value:
            # Validate staff_id
            staff_id = item.get("staff_id")
            if staff_id is None:
                raise serializers.ValidationError("staff_id is required.")
            if not isinstance(staff_id, int):
                raise serializers.ValidationError(f"Invalid staff_id '{staff_id}': must be an integer.")
            staff_ids.append(staff_id)

            # Validate given_treatment list
            given_treatment = item.get("given_treatment", [])
            if not given_treatment:
                raise serializers.ValidationError("given_treatment list cannot be empty.")

            for treatment in given_treatment:
                medicine_data = treatment.get("medicine_data")
                if medicine_data is None:
                    raise serializers.ValidationError("medicine_data is required in each treatment.")
                if not isinstance(medicine_data, int):
                    raise serializers.ValidationError(f"Invalid medicine_data '{medicine_data}': must be an integer.")
                medicine_ids.append(medicine_data)

        # Validate existence of staff IDs
        existing_staff = set(Staff.objects.filter(id__in=staff_ids).values_list("id", flat=True))
        missing_staff = [sid for sid in staff_ids if sid not in existing_staff]
        if missing_staff:
            raise serializers.ValidationError(f"staff_id(s) not found: {missing_staff}")

        # Validate existence of medicine IDs
        existing_meds = set(medicine.objects.filter(id__in=medicine_ids).values_list("id", flat=True))
        missing_meds = [mid for mid in medicine_ids if mid not in existing_meds]
        if missing_meds:
            raise serializers.ValidationError(f"medicine_data ID(s) not found: {missing_meds}")

        return value


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
        
        instance.referred_by = validated_data.get('referred_by', instance.referred_by)
        instance.date_of_refer = validated_data.get('date_of_refer', instance.date_of_refer)
        instance.advice = validated_data.get('advice', instance.advice)
        instance.discharge_condition = validated_data.get('discharge_condition', instance.discharge_condition)

        new_payment_details = validated_data.get('payment_details')
        if new_payment_details:
            if isinstance(instance.payment_details, list):
                instance.payment_details.extend(new_payment_details)
            else:
                instance.payment_details = new_payment_details 
        
        new_past_historys = validated_data.get('past_historys')
        if new_past_historys:
            if isinstance(instance.past_historys, list):
                instance.past_historys.extend(new_past_historys)
            else:
                instance.past_historys = new_past_historys

        new_daily_chief_complaints = validated_data.get('daily_chief_complaints')
        if new_daily_chief_complaints:
            if isinstance(instance.daily_chief_complaints, list):
                instance.daily_chief_complaints.extend(new_daily_chief_complaints)
            else:
                instance.daily_chief_complaints = new_daily_chief_complaints   

        new_systemetic_examination = validated_data.get('systemetic_examination')
        if new_systemetic_examination:
            if isinstance(instance.systemetic_examination, list):
                instance.systemetic_examination.extend(new_systemetic_examination)
            else:
                instance.systemetic_examination = new_systemetic_examination    

        new_general_examination = validated_data.get('general_examination')
        if new_general_examination:
            if isinstance(instance.general_examination, list):
                instance.general_examination.extend(new_general_examination)
            else:
                instance.general_examination = new_general_examination    
        new_daily_examination = validated_data.get('daily_examination')
        if new_daily_examination:
            if isinstance(instance.daily_examination, list):
                instance.daily_examination.extend(new_daily_examination)
            else:
                instance.daily_examination = new_daily_examination                       
        new_given_medicine = validated_data.get('given_medicine')
        if new_given_medicine:
            if isinstance(instance.given_medicine, list):
                instance.given_medicine.extend(new_given_medicine)
            else:
                instance.given_medicine = new_given_medicine
        new_daily_given_treatment = validated_data.get('daily_given_treatment')
        if new_daily_given_treatment:
            if isinstance(instance.daily_given_treatment, list):
                instance.daily_given_treatment.extend(new_daily_given_treatment)
            else:
                instance.daily_given_treatment = new_daily_given_treatment        
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["bed_data"] = bed_serializers(instance.bed_data).data  
        representation["doctor_data"] = DoctorSerializer(instance.doctor_data).data 
        
        # Reusable staff enrichment helper
        def enrich_staff(item, key="staff_data"):
            staff_id = item.get(key)
            if staff_id:
                try:
                    staff = Staff.objects.get(id=staff_id)
                    item[key] = {
                        "id": staff.id,
                        "staff_name": staff.staff_name,
                        "department": staff.department,
                        "mobile_no": staff.mobile_no,
                    }
                except Staff.DoesNotExist:
                    item[key] = None
            return item

        # payment_details
        representation["payment_details"] = [
            enrich_staff(item, key="staff_data")
            for item in representation.get("payment_details", [])
        ]

        # general_examination
        representation["general_examination"] = [
            enrich_staff(item, key="staff_data")
            for item in representation.get("general_examination", [])
        ]

        # systemetic_examination
        representation["systemetic_examination"] = [
            enrich_staff(item, key="staff_data")
            for item in representation.get("systemetic_examination", [])
        ]

        # daily_given_treatment (uses 'staff_id' instead of 'staff_data')
        representation["daily_given_treatment"] = [
            enrich_staff(item, key="staff_id")
            for item in representation.get("daily_given_treatment", [])
        ]

        representation["daily_examination"] = [
            enrich_staff(item, key="staff_data")
            for item in representation.get("daily_examination", [])
        ]
        
        def enrich_past_history(item, key="past_history_data"):
            history_id = item.get(key)
            if history_id:
                try:
                    history = past_history.objects.get(id=history_id)
                    item[key] = {
                        "id": history.id,
                        "name": history.name  # adjust field names as per your model
                       
                    }
                except past_history.DoesNotExist:
                    item[key] = None
            return item

        # Apply past_history enrichment
        representation["past_historys"] = [
            enrich_past_history(item)
            for item in representation.get("past_historys", [])
        ]

        def enrich_complaints(daily_item):
            for complaints in daily_item.get("chief_complaints", []):
                cid = complaints.get("complaints_data")
                if cid:
                    try:
                        complaint_obj = complaint.objects.get(id=cid)
                        complaints["complaints_data"] = {
                            "id": complaint_obj.id,
                            "name": complaint_obj.name # replace with real fields
                            
                        }
                    except complaint.DoesNotExist:
                        complaints["complaints_data"] = None
            return daily_item

        # Apply to each daily_chief_complaints item
        representation["daily_chief_complaints"] = [
            enrich_complaints(item)
            for item in representation.get("daily_chief_complaints", [])
        ]

        def enrich_medicine(item, key="medicine_data"):
            med_id = item.get(key)
            if med_id:
                try:
                    medicines = medicine.objects.get(id=med_id)
                    item[key] = {
                        "id": medicines.id,
                        "medicine_name": medicines.medicine_name
                    
                    }
                except medicine.DoesNotExist:
                    item[key] = None
            return item

        # ✅ Enrich given_medicine list
        representation["given_medicine"] = [
            enrich_medicine(item)
            for item in representation.get("given_medicine", [])
        ]

        # ✅ Enrich nested given_treatment inside daily_given_treatment
        for treatment_entry in representation.get("daily_given_treatment", []):
            treatment_entry["given_treatment"] = [
                enrich_medicine(item)
                for item in treatment_entry.get("given_treatment", [])
            ]
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
    date = serializers.CharField(max_length=250,required=False)
    total_amount = serializers.FloatField(required=False)
    
    chief_complaints = serializers.JSONField(required=False) 
    vitals = serializers.JSONField(required=False) 
    examination = serializers.JSONField(required=False) 
    given_medicine = serializers.JSONField(required=False) 
    diagnosis_detail = serializers.JSONField(required=False) 
   

    class Meta:
        model = OPD
        fields = '__all__'
    #     read_only_fields = ['date']
    # def get_date(self, obj):
    #     local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
    #     local_dt = obj.date.astimezone(local_tz)
    #     return local_dt.strftime('%Y-%m-%d %H:%M:%S')        

    def validate_vitals(self, value):
        required_keys = {"BP", "PR", "SPO", "Sugar"}

        missing_keys = required_keys - value.keys()
        if missing_keys:  
            raise serializers.ValidationError(f"Missing keys: {', '.join(missing_keys)}")

        for key in required_keys:
            if not isinstance(value.get(key), (int, float)):
                raise serializers.ValidationError(f"Invalid value type for {key}. Must be int or float.")

        return value


    def validate_diagnosis_detail(self, value):
       
        if value is None:
            raise serializers.ValidationError("diagnosis ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("diagnosis_data")
            if cid is None:
                raise serializers.ValidationError("diagnosis ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for diagnosis ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            diagnosis.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Diagnosis(s) with ID(s) {missing_ids} not found in the diagnosis master list."
            )

        return value  
    def validate_chief_complaints(self, value):
       
        if value is None:
            raise serializers.ValidationError("Complaint ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("complaints_data")
            if cid is None:
                raise serializers.ValidationError("Complaint ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for complaint ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            complaint.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Complaint(s) with ID(s) {missing_ids} not found in the complaints master list."
            )

        return value
    def validate_given_medicine(self, value):
       
        if value is None:
            raise serializers.ValidationError("Medicine ID list cannot be null.")

        # Extract all complaint IDs from the input
        complaint_ids = []
        for item in value:
            cid = item.get("medicine_data")
            if cid is None:
                raise serializers.ValidationError("Medicine ID cannot be null.")
            if not isinstance(cid, int):
                raise serializers.ValidationError(
                    f"Invalid format for Medicine ID: '{cid}'. Must be an integer."
                )
            complaint_ids.append(cid)

        # Query the database for these IDs
        existing_ids = list(
            medicine.objects.filter(id__in=complaint_ids).values_list("id", flat=True)
        )

        # Find any IDs that do not exist
        missing_ids = []
        for cid in complaint_ids:
            if cid not in existing_ids:
                missing_ids.append(cid)

        if missing_ids:
            raise serializers.ValidationError(
                f"Medicine(s) with ID(s) {missing_ids} not found in the Medicine list."
            )

        return value
    
      
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
        instance.date = validated_data.get('date', instance.date)
        service_data = validated_data.pop('service_id', None)
        if service_data is not None:
            instance.service_id.set(service_data)
      
        
        new_chief_complaints = validated_data.get('chief_complaints')
        if new_chief_complaints:
            if isinstance(instance.chief_complaints, list):
                instance.chief_complaints.extend(new_chief_complaints)
            else:
                instance.chief_complaints = new_chief_complaints 
        new_vitals = validated_data.get('vitals')
        if new_vitals:
            existing_vitals = instance.vitals or {}
            existing_vitals.update(new_vitals)
            instance.vitals = existing_vitals 
        new_examination = validated_data.get('examination')
        if new_examination:
            existing_examination = instance.examination or {}
            existing_examination.update(new_examination)
            instance.examination = existing_examination  
        new_given_medicine = validated_data.get('given_medicine')
        if new_given_medicine:
            if isinstance(instance.given_medicine, list):
                instance.given_medicine.extend(new_given_medicine)
            else:
                instance.given_medicine = new_given_medicine 
        new_diagnosis_detail = validated_data.get('diagnosis_detail')
        if new_diagnosis_detail:
            if isinstance(instance.diagnosis_detail, list):
                instance.diagnosis_detail.extend(new_diagnosis_detail)
            else:
                instance.diagnosis_detail = new_diagnosis_detail          
 
        
        instance.save()
        return instance
    


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["service_id"] = ServiceSerializer(instance.service_id,many=True).data  
        representation["doctor_data"] = DoctorSerializer(instance.doctor_data).data  
       
        chief_complaints_data = representation.get('chief_complaints')
        if chief_complaints_data and isinstance(chief_complaints_data, list):
            processed_complaints = []
            for entry in chief_complaints_data:
                complaint_id = entry.get('complaints_data')
                complaint_obj = complaint.objects.get(id=complaint_id)
                mapped_complaint_data = {
                    "id": complaint_obj.id,
                    "name": complaint_obj.name
                }
                entry['complaints_data'] = mapped_complaint_data
                processed_complaints.append(entry)
            
            representation['chief_complaints'] = processed_complaints
        given_medicine_data = representation.get('given_medicine')
        if given_medicine_data and isinstance(given_medicine_data, list):
            processed_complaints = []
            for entry in given_medicine_data:
                complaint_id = entry.get('medicine_data')
                complaint_obj = medicine.objects.get(id=complaint_id)
                mapped_complaint_data = {
                    "id": complaint_obj.id,
                    "name": complaint_obj.medicine_name
                }
                entry['medicine_data'] = mapped_complaint_data
                processed_complaints.append(entry)
            
            representation['given_medicine'] = processed_complaints
        given_diagnosis_detail = representation.get('diagnosis_detail')
        if given_diagnosis_detail and isinstance(given_diagnosis_detail, list):
            processed_complaints = []
            for entry in given_diagnosis_detail:
                complaint_id = entry.get('diagnosis_data')
                complaint_obj = diagnosis.objects.get(id=complaint_id)
                mapped_complaint_data = {
                    "id": complaint_obj.id,
                    "diagnosis_name": complaint_obj.diagnosis_name
                }
                entry['diagnosis_data'] = mapped_complaint_data
                processed_complaints.append(entry)
            
            representation['diagnosis_detail'] = processed_complaints    

        
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
    date_of_joining = serializers.CharField(max_length=250,required=False)
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ['date_of_joining']
    # def get_date_of_joining(self, obj):
    #     local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
    #     local_dt = obj.date_of_joining.astimezone(local_tz)
    #     return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    def create(self, validated_data):
        return Doctor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.doctor_name = validated_data.get('doctor_name', instance.doctor_name)
        instance.specialization_id = validated_data.get('specialization_id', instance.specialization_id)
        instance.date_of_joining = validated_data.get('date_of_joining', instance.date_of_joining)
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
    date_of_joining = serializers.CharField(max_length=250,required=False)


    class Meta:
        model = Staff
        fields = '__all__'
    #     read_only_fields = ['date_of_joining']
    # def get_date_of_joining(self, obj):
    #     local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
    #     local_dt = obj.date_of_joining.astimezone(local_tz)
    #     return local_dt.strftime('%Y-%m-%d %H:%M:%S')        
        
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

class medicine_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    medicine_name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=medicine
        fields ='__all__'
        

    def create(self, validated_data):
        return medicine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.medicine_name=validated_data.get('medicine_name',instance.medicine_name)
        instance.save()
        return instance         




class diagnosis_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    diagnosis_name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=diagnosis
        fields ='__all__'
        

    def create(self, validated_data):
        return diagnosis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.diagnosis_name=validated_data.get('diagnosis_name',instance.diagnosis_name)
        instance.save()
        return instance     