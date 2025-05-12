
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
        return representation        



class scalp_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
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
        instance.save()
        return instance







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


class PatientConditionSerializer(serializers.ModelSerializer):
    complaints = serializers.PrimaryKeyRelatedField(queryset=complaint.objects.all(), many=True)
    past_history = serializers.PrimaryKeyRelatedField(queryset=past_history.objects.all(), many=True)
    personal_H_O = serializers.PrimaryKeyRelatedField(queryset=personal_H_O.objects.all(), many=True)

    class Meta:
        model = PatientCondition
        fields = [
            'complaints', 'past_history', 'personal_H_O',
            'poller', 'icterus', 'LAP', 'clubbing', 'cyanosis'
        ]

class FCSerializer(serializers.ModelSerializer):
    patient_condition = PatientConditionSerializer()

    class Meta:
        model = FC
        fields = [
            'referrer', 'patient_name', 'age', 'gender',
            'address', 'mobile_no', 'patient_condition', 'Opinion'
        ]

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

