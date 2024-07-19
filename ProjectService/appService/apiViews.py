from appService.models import *
from .views import generarPassword
# work
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appService.serializers import OficinaSerializer, UserSerializer


class OficinaList(generics.ListCreateAPIView):
    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer


class OficinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer


class UserList(generics.ListCreateAPIView):
    queryset =Usuario.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class Oficina_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Oficina.objects.all()
        serializer = OficinaSerializer(post, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OficinaSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.ofiNombre)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApi(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            datosValidos = serializer.validated_data
            first_name = datosValidos['first_name']
            last_name = datosValidos['last_name']
            email = datosValidos['email']
            userTipo = datosValidos['tipoUsuario']
            username = datosValidos['username']
            userFoto = datosValidos['foto']
            user = Usuario(**datosValidos)
            user.save()
            passwordGenerado = generarPassword()
            print(f"password {passwordGenerado}")
            user.set_password(passwordGenerado)
            # se actualiza el user
            user.save()
            serializer_response = UserSerializer(user)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)