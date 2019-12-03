from rest_framework import routers, serializers, viewsets

# -------------AGREGANDO MODELOS-----------------
from registro.models import Registro

class RegistroSerializers(serializers.ModelSerializer):
    



    class Meta:
        model = Registro
        fields = ('__all__')