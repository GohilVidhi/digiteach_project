
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

   