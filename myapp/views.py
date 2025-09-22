from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import * 
from .serializers import * 
from rest_framework import status

# Create your views here.


class test(APIView):
    def get(self,request):
        return Response({"msg":"Digiteach Project"})


# ===============pagination code==========================

from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 100  # You can change this number
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


class Designation_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Designation.objects.get(id=id)
                serializer = Designation_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Designation.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Designation.objects.all().order_by("-id")
            # serializer = Designation_serializers(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, Designation_serializers, CustomPagination)

    def post(self, request):
        serializer = Designation_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Designation.objects.get(id=id)
        except Designation.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = Designation_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Designation.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Designation.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        



class School_view(APIView):
    def get(self, request, id=None,designation_id=None):
        if id:
            try:
                uid = School.objects.get(id=id)
                serializer = School_Serializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except School.DoesNotExist:
                return Response({'status': "Invalid"})
            
        elif designation_id:
            try:
                uid = School.objects.filter(designation_data__id=designation_id)
                # serializer = School_Serializer(uid,many=True)
                # return Response({'status': 'success', 'data': serializer.data})
                return get_paginated_result(uid, request, School_Serializer, CustomPagination)
            except School.DoesNotExist:
                return Response({'status': "Invalid"}) 
        else:
            uid = School.objects.all().order_by("-id")
            # serializer = School_Serializer(uid, many=True)
            # return Response({'status': 'success', 'data': serializer.data})
            return get_paginated_result(uid, request, School_Serializer, CustomPagination)

    def post(self, request):
        serializer = School_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = School.objects.get(id=id)
        except School.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = School_Serializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = School.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except School.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        


