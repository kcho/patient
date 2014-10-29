####### django default #######
from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict

# --- auth
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# -- erorr, response
from django.http import Http404


####### my models #######
from mrCheck.models import *

##### REST framework ######
from rest_framework.views import APIView

# --- auth
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# --- serializers
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Patient

# -- error, response
from rest_framework.response import Response
from rest_framework import status


####### utils ########

import json

# Create your views here.

def toJSON(objs, status=200):
    j = json.dumps(objs, ensure_ascii=False)
    return HttpResponse(j, status=status, content_type='application/json; charset=utf-8')



class patient_view(APIView) :
    # get patient list
    def get(self, request, format=None) :
        sts = Patient.objects.all()
        serializer = PatientSerializer(sts, many=True)

        return Response(serializer.data)


    def post(self, request, format=None) :
        serializer = PatientSerializer(data=request.DATA)
        if serializer.is_valid() :
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class patient_detail_view(APIView) :

    def get_object(self, id):
        try:
            return Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            raise Http404


    def get(self, request, id, format=None) :
        st = self.get_object(id)
        serializer = PatientSerializer(st)

        return Response(serializer.data)


    def put(self, request, id, format=None) :
        st = self.get_object(id)
        serializer = PatientSerializer(st, data=request.DATA)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None) :
        st = self.get_object(id)
        st.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

