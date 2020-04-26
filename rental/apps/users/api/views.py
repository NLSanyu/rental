from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "Registration successful"
        data['username'] = user.username
    else:
        data = serializer.errors
    return Response(data)