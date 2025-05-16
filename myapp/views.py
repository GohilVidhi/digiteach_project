from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import * 
from .serializers import * 
# Create your views here.


class test(APIView):
    def get(self,request):
        return Response({"msg":"Done"})


# ===============pagination code==========================

from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 1  # You can change this number
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({
           
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
def get_paginated_result(queryset, request, serializer_class, paginator_class):
    paginator = paginator_class()
    page = paginator.paginate_queryset(queryset, request)
    serializer = serializer_class(page, many=True)
    return paginator.get_paginated_response(serializer.data) 

# ===============pagination code end==========================


class bed_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = bed.objects.get(id=id)
                serializer = bed_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except bed.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = bed.objects.all().order_by("-id")
            # serializer = bed_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, bed_serializers, CustomPagination)

    def post(self, request):
        serializer = bed_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = bed.objects.get(id=id)
        except bed.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = bed_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = bed.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except bed.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        


class ipd_view(APIView):
    def get(self, request, id=None , bed_id=None):
        if id:
            try:
                uid = ipd.objects.get(id=id)
                serializer = ipd_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except ipd.DoesNotExist:
                return Response({'status': "Invalid"})
        elif bed_id:
            try:
                uid = ipd.objects.filter(bed_data__id=bed_id)
        
                # serializer = ipd_serializers(uid,many=True)
                # return Response({'status': 'success', 'data': serializer.data})
                return get_paginated_result(uid, request, ipd_serializers, CustomPagination)

            except ipd.DoesNotExist:
                return Response({'status': "Invalid"})    
        else:
            uid = ipd.objects.all().order_by("-id")
            # serializer = ipd_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, ipd_serializers, CustomPagination)

    def post(self, request):
        serializer = ipd_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = ipd.objects.get(id=id)
        except ipd.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = ipd_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = ipd.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except ipd.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})



class scalp_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = scalp.objects.get(id=id)
                serializer = scalp_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except scalp.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = scalp.objects.all().order_by("-id")
            # serializer = scalp_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, scalp_serializers, CustomPagination)


    def post(self, request):
        serializer = scalp_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = scalp.objects.get(id=id)
        except scalp.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = scalp_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = scalp.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except scalp.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        





#====================
class complaint_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = complaint.objects.get(id=id)
                serializer = complaint_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except complaint.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = complaint.objects.all().order_by("-id")
            # serializer = complaint_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, complaint_serializers, CustomPagination)


    def post(self, request):
        serializer = complaint_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = complaint.objects.get(id=id)
        except complaint.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = complaint_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = complaint.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except complaint.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
        
#-----------=========================
class past_history_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = past_history.objects.get(id=id)
                serializer = past_history_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except past_history.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = past_history.objects.all().order_by("-id")
            # serializer = past_history_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, past_history_serializers, CustomPagination)

            

    def post(self, request):
        serializer = past_history_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = past_history.objects.get(id=id)
        except past_history.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = past_history_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = past_history.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except past_history.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
        
#================

class personal_H_O_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = personal_H_O.objects.get(id=id)
                serializer = personal_H_O_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except personal_H_O.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = personal_H_O.objects.all().order_by("-id")
            # serializer = personal_H_O_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, personal_H_O_serializers, CustomPagination)


    def post(self, request):
        serializer = personal_H_O_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = personal_H_O.objects.get(id=id)
        except personal_H_O.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = personal_H_O_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = personal_H_O.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except personal_H_O.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        

class fc_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = FC.objects.get(id=id)
                serializer = FCSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except FC.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = FC.objects.all().order_by("-id")
            # serializer = FCSerializer(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, FCSerializer, CustomPagination)


    def post(self, request):
        serializer = FCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = FC.objects.get(id=id)
        except FC.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = FCSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = FC.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except FC.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})





#======================admin_login_view=======================
from rest_framework_simplejwt.tokens import RefreshToken        
class admin_login_view(APIView):
    def get(self,request,id=None , email=None):
        if id:

            try:
                uid=admin_login.objects.get(id=id)
                serializer=admin_login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid email"})
        elif email:

            try:
                uid=admin_login.objects.get(email=email)
                serializer=admin_login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid email"})
        else:
            uid=admin_login.objects.all().order_by("-id")
            serializer=admin_login_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})

    def post(self, request):
        serializer = admin_login_serializers(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email', None)
            mobile_no = serializer.validated_data.get('mobile_no', None)
            password = serializer.validated_data.get('password')

            # Try to get the user by email or mobile
            try:
                if email:
                    user = admin_login.objects.get(email=email)
                elif mobile_no:
                    user = admin_login.objects.get(mobile_no=mobile_no)
                else:
                    return Response({'status': 'email or mobile is required'}, status=400)

                # Raw password match (replace with `check_password` if using hashing)
                if user.password == password:
                    refresh = RefreshToken.for_user(user)
                    response_serializer = admin_login_serializers(user)
                    return Response({
                        'status': 'success',
                        'data': response_serializer.data,
                        'token': str(refresh.access_token)
                    })
                else:
                    return Response({'status': 'invalid password'})

            except admin_login.DoesNotExist:
                return Response({'status': 'invalid email or mobile'})

        return Response({'status': 'invalid data', 'errors': serializer.errors})


    # def patch(self,request,id=None):
    #     try:
    #         uid=admin_login.objects.get(id=id)
    #     except:
    #         return Response({'status':"invalid email"})
    #     serializer=admin_login_serializers(uid,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status':'success','data':serializer.data})
    #     else:
    #         return Response({'status':"invalid email"})
    # def delete(self,request,id=None,email=None):
    #     if id:
    #         try:
    #             uid=admin_login.objects.get(id=id)
    #             uid.delete()
    #             return Response({'status':'Deleted data'})
    #         except:
    #             return Response({'status':"invalid id"})
    #     elif email:
    #         del request.session['email']
    #         return Response({'status': 'Logged out successfully'})

    #     else:
    #         return Response({'status':"invalid data"})

#==================
class Service_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Service.objects.get(id=id)
                serializer = ServiceSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Service.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Service.objects.all().order_by("-id")
            # serializer = ServiceSerializer(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, ServiceSerializer, CustomPagination)


    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Service.objects.get(id=id)
        except Service.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = ServiceSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Service.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Service.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
#=============
class Specialization_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Specialization.objects.get(id=id)
                serializer = SpecializationSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Specialization.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Specialization.objects.all().order_by("-id")
            # serializer = SpecializationSerializer(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, SpecializationSerializer, CustomPagination)


    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Specialization.objects.get(id=id)
        except Specialization.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = SpecializationSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Specialization.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Specialization.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
        
#===================
class Doctor_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Doctor.objects.get(id=id)
                serializer = DoctorSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Doctor.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Doctor.objects.all().order_by("-id")
            # serializer = DoctorSerializer(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, DoctorSerializer, CustomPagination)
            
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = DoctorSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Doctor.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Doctor.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
#========================
class OPD_view(APIView):
    def get(self, request, id=None,doctor_id=None):
        if id:
            try:
                uid = OPD.objects.get(id=id)
                serializer = OPDSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except OPD.DoesNotExist:
                return Response({'status': "Invalid"})
        elif doctor_id:
            try:
                uid = OPD.objects.filter(doctor_data__id=doctor_id)
                # serializer = OPDSerializer(uid,many=True)
                # return Response({'status': 'success', 'data': serializer.data})
                return get_paginated_result(uid, request, OPDSerializer, CustomPagination)
            except OPD.DoesNotExist:
                return Response({'status': "Invalid"})    
        else:
            uid = OPD.objects.all().order_by("-id")
            # serializer = OPDSerializer(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, OPDSerializer, CustomPagination)
            

    def post(self, request):
        serializer = OPDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = OPD.objects.get(id=id)
        except OPD.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = OPDSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = OPD.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except OPD.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

