
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



class Job_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    school_data = serializers.SlugRelatedField(slug_field="id",
        queryset=School.objects.all(),
        required=True,
        allow_null=False
    )
    job_title = serializers.CharField(max_length=255, required=True, allow_blank=False)
    job_description = serializers.CharField(required=True, allow_blank=False)
    job_type = serializers.CharField(max_length=255, required=True, allow_blank=False)
    subject = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    experience_required = serializers.CharField(max_length=50, required=False, allow_blank=True, allow_null=True)
    qualification = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    salary_range = serializers.CharField(max_length=50, required=False, allow_blank=True, allow_null=True)
    posted_date = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    last_date_to_apply = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    status = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)

    
    def create(self, validated_data):
        return Job.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.school_data = validated_data.get("school_data", instance.school_data)
        instance.job_title = validated_data.get("job_title", instance.job_title)
        instance.job_description = validated_data.get("job_description", instance.job_description)
        instance.job_type = validated_data.get("job_type", instance.job_type)
        instance.subject = validated_data.get("subject", instance.subject)
        instance.experience_required = validated_data.get("experience_required", instance.experience_required)
        instance.qualification = validated_data.get("qualification", instance.qualification)
        instance.salary_range = validated_data.get("salary_range", instance.salary_range)
        instance.posted_date = validated_data.get("posted_date", instance.posted_date)
        instance.last_date_to_apply = validated_data.get("last_date_to_apply", instance.last_date_to_apply)
        instance.status = validated_data.get("status", instance.status)

        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["school_data"] = School_Serializer(instance.school_data).data if instance.school_data else None
        
        return representation
    
    

#============================


class Teacher_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    teacher_id = serializers.CharField(max_length=20, required=False, read_only=True)
    full_name = serializers.CharField(max_length=255, required=False, allow_null=True)
    email = serializers.EmailField(required=False, allow_null=True)
    mobile = serializers.CharField(max_length=20, required=False, allow_null=True)
    dob = serializers.CharField(max_length=255, required=False, allow_null=True)
    gender = serializers.CharField(max_length=10, required=False, allow_null=True)
    address = serializers.JSONField(required=False, allow_null=True)
    qualification = serializers.CharField(max_length=255, required=False, allow_null=True)
    experience = serializers.CharField(max_length=50, required=False, allow_null=True)

    subjects = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_null=True),
        required=False, allow_null=True
    )
    preferred_classes = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_null=True),
        required=False, allow_null=True
    )

    resume_url = serializers.FileField(required=False, allow_null=True)
    profile_image = serializers.ImageField(required=False, allow_null=True)
    youtube_link = serializers.URLField(required=False, allow_null=True)

    expected_salary = serializers.CharField(max_length=50, required=False, allow_null=True)
    availability = serializers.CharField(max_length=50, required=False, allow_null=True)

    skills = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_null=True),
        required=False, allow_null=True
    )
    languages_known = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_null=True),
        required=False, allow_null=True
    )

    created_at = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(max_length=10, required=False, allow_null=True)



    def generate_teacher_id(self):
        """Generate a sequential teacher ID like T1001, T1002, etc."""
        last_teacher = Teacher.objects.order_by("-id").first()
        new_id = 1001  # default starting number

        if last_teacher and last_teacher.teacher_id.startswith("T"):
            # safely get numeric part
            numeric_part = ''.join(filter(str.isdigit, last_teacher.teacher_id))
            if numeric_part:
                new_id = int(numeric_part) + 1

        return f"T{new_id}"

    def validate_address(self, value):
        """
        Validate that the address contains required keys: locality, city, state, pincode
        """
        if value in [None, {}, ""]:   # <-- allow null/empty
            return value

        required_keys = ["locality", "city", "state", "pincode"]
        missing_keys = [key for key in required_keys if key not in value]
        if missing_keys:
            raise serializers.ValidationError(
                f"Missing keys in address: {', '.join(missing_keys)}"
            )

        # Optional: Validate pincode is numeric
        if not str(value.get("pincode", "")).isdigit():
            raise serializers.ValidationError("Pincode must be numeric.")

        return value

    def create(self, validated_data):
        validated_data['teacher_id'] = self.generate_teacher_id()
        return Teacher.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        # instance.teacher_id = validated_data.get("teacher_id", instance.teacher_id)
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.email = validated_data.get("email", instance.email)
        instance.mobile = validated_data.get("mobile", instance.mobile)
        instance.dob = validated_data.get("dob", instance.dob)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.address = validated_data.get("address", instance.address)
        instance.qualification = validated_data.get("qualification", instance.qualification)
        instance.experience = validated_data.get("experience", instance.experience)
        instance.subjects = validated_data.get("subjects", instance.subjects)
        instance.preferred_classes = validated_data.get("preferred_classes", instance.preferred_classes)
        instance.resume_url = validated_data.get("resume_url", instance.resume_url)
        instance.profile_image = validated_data.get("profile_image", instance.profile_image)
        instance.youtube_link = validated_data.get("youtube_link", instance.youtube_link)
        instance.expected_salary = validated_data.get("expected_salary", instance.expected_salary)
        instance.availability = validated_data.get("availability", instance.availability)
        instance.skills = validated_data.get("skills", instance.skills)
        instance.languages_known = validated_data.get("languages_known", instance.languages_known)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        """custom representation"""
        data = super().to_representation(instance)

        for field in ["subjects", "preferred_classes", "skills", "languages_known"]:
            if data.get(field) is None:
                data[field] = []   # list -> []

        if data.get("address") is None:
            data["address"] = {}   # json -> {}

       
        return data
    
    
class Apply_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    job_data = serializers.SlugRelatedField(slug_field="id",
        queryset=Job.objects.all(),
        required=True,
        allow_null=False
    )
    teacher_data = serializers.SlugRelatedField(slug_field="teacher_id",
        queryset=Teacher.objects.all(),
        required=True,
        allow_null=False
    )
    applied_date = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Job_Apply.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.job_data = validated_data.get('job_data', instance.job_data)
        instance.teacher_data = validated_data.get('teacher_data', instance.teacher_data)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation["teacher_data"] = Teacher_Serializer(instance.teacher_data).data if instance.teacher_data else None
        
        representation["job_data"] = Job_Serializer(instance.job_data).data if instance.job_data else None  
        return representation