from rest_framework.viewsets import ModelViewSet
from car.models import Car
from .serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated

class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    filterset_fields = ('plate_number','year','color','model')
    #permission_classes = [IsAuthenticated] 
    

    def destroy(self, request, *args, **kwargs):
        Car.objects.filter(pk=kwargs['pk']).update(active=False)
        