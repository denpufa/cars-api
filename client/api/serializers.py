from rest_framework.serializers import ModelSerializer
from client.models import Client

class ClientSerializer(ModelSerializer) :
    class Meta :
        model = Client
        fields = [
            'nome','telefone','email','password'
        ]