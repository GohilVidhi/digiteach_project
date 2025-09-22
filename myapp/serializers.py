
from rest_framework import serializers
from .models import *
class Designation_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
   

    class Meta:
        models=Designation
        fields ='__all__'
        

    def create(self, validated_data):
        return Designation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance      
    
    
    
class School_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    school_name = serializers.CharField(max_length=250, required=False, allow_null=True, allow_blank=True)
    school_email = serializers.EmailField(max_length=250, required=False, allow_null=True, allow_blank=True)
    school_address = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    contact_person_name = serializers.CharField(max_length=250, required=False, allow_null=True, allow_blank=True)
    contact_number = serializers.IntegerField(required=False, allow_null=True)
    designation_data = serializers.SlugRelatedField(
        slug_field="id",
        queryset=Designation.objects.all()
    )
    address_line_1 = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    address_line_2 = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    landmark = serializers.CharField(max_length=250, required=False, allow_null=True, allow_blank=True)
    city = serializers.CharField(max_length=250, required=False, allow_null=True, allow_blank=True)
    district = serializers.CharField(max_length=250, required=False, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.school_name = validated_data.get("school_name", instance.school_name)
        instance.school_email = validated_data.get("school_email", instance.school_email)
        instance.school_address = validated_data.get("school_address", instance.school_address)
        instance.contact_person_name = validated_data.get("contact_person_name", instance.contact_person_name)
        instance.contact_number = validated_data.get("contact_number", instance.contact_number)
        instance.designation_data = validated_data.get("designation_data", instance.designation_data)
        instance.address_line_1 = validated_data.get("address_line_1", instance.address_line_1)
        instance.address_line_2 = validated_data.get("address_line_2", instance.address_line_2)
        instance.landmark = validated_data.get("landmark", instance.landmark)
        instance.city = validated_data.get("city", instance.city)
        instance.district = validated_data.get("district", instance.district)
        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["designation_data"] = Designation_serializers(instance.designation_data).data if instance.designation_data else None
        
        return representation
