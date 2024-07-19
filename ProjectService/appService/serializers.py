from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from appService.models import *


class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = '__all__'


class TipoProcedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcedimiento
        fields = ('id', 'nombre', 'descripcion',
                'fechaHoraCreacion', 'fechaHoraActualizacion')


class UsuarioSerializer(serializers.ModelSerializer):
    foto = Base64ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name','email', ' tipoUsuario ', 'foto')