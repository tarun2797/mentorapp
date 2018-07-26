from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from onlineapp.models import *
from onlineapp.serializers import *

@api_view(['GET', 'POST'])
def college_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        colleges = college.objects.all()
        serializer = collegeSerializer(colleges, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        college_data = collegeSerializer(data=request.query_params)
        #import ipdb
        print(request.query_params)
        if college_data.is_valid():
            college_data.save()
            return Response(college_data.data, status=status.HTTP_201_CREATED)
        return Response(college_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def college_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        college_data = college.objects.get(pk=pk)
    except college.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = collegeSerializer(college_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #print("request data = ",request.data)
        data = JSONParser().parse(request)
        serializer = collegeSerializer(college_data, data=data)
        print(" data = ",data)
        print("request = ",request)
        print(" serializer = ",serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        college_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class college_students(APIView):

    def get_object(self, pk):
        try:
            L = Student.objects.filter(college__id=pk)
            #print(L)
            return L
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        #college_data = self.get_object(pk)
        #print("clg_id = ",pk)
        student_data = Student.objects.all().filter(college__id=pk)
        #print("snippet = ",student_data)
        #import ipdb
        #ipdb.set_trace()
        serializer = StudentSerializer(student_data,many=True)
        return Response(serializer.data)

    def post(self,request,pk,format=None):
        serializer = StudentSerializer(data=request.data)
        print("serialized data = ",serializer)
        if serializer.is_valid():
            #print("post data = ",serializer.validated_data)
            serializer.validated_data['college_id'] = pk
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class student_detail(APIView):
    pass
    def get_object(self, pk,id):
        try:
            student_data = Student.objects.get(pk=id)
            if student_data.college_id==pk:
                return student_data
            else:
                raise Http404
        except student_data.DoesNotExist:
            raise Http404

    def get(self, request, pk, id,format=None):
        stud_list = self.get_object(pk, id)
        serializer = StudentSerializer(stud_list)
        return Response(serializer.data)

    def put(self, request, pk,id,format=None):
        stud_list = self.get_object(pk,id)
        serializer = StudentSerializer(stud_list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk,id, format=None):
        stud_list = self.get_object(pk,id)
        stud_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)