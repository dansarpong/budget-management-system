from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *



class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = Userserializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                print("data saved")
                return Response ({
                        'status': 200,
                        'message': 'Registration successful. Check email.',
                        'data': serializer.data,})
               
            return Response({
                'status': 400,
                'message':'Something went wrong',
                'data': serializer.errors,
            })

        except Exception as e:
            print(e)