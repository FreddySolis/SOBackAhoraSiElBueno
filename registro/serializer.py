from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from registro.models import Registro
from carrera.serializer import CarreraSerializers

class RegistroSerializers(serializers.ModelSerializer):
    
    #carrera = serializers.ReadOnlyField(source='carrera.name')
    #carrera = serializers.StringRelatedField(many=True)
    carrera = CarreraSerializers(many=False, read_only=True)
    carrera_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = Registro
        fields = ('__all__')