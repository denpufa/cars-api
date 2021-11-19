from rest_framework.viewsets import ModelViewSet
from .serializers import ClientSerializer
from client.models import Client
class ClientViewSet(ModelViewSet) :
    queryset = Client.objects.all()
    serializer_class = ClientSerializer 
    

