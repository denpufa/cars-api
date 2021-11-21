from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from car.models import Car
from .serializers import CarSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication 

class CarListedView(APIView):
    
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self,request): 
        cars = Car.objects.filter(owner=request.user,active=True)
        serializer = CarSerializer(data=cars,many=True)
        if serializer.is_valid() :
            return Response(serializer.data)
        return Response({})
    
    def post(self,request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class CarDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    
    
    def get(self, request,plate) :
        try:
            car = Car.objects.get(owner=request.user,plate_number=plate,active=True)
        except Car.DoesNotExist:
            return Response({"error":"not found car with this plate"},status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(data=car)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response({"erro":"the server has a error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request,plate):
        try:
            car = Car.objects.get(plate_number=plate,active=True)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(instance=car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,plate):    
        try:
            car = Car.objects.get(plate_number=plate,active=True).update(active=False)
        except Car.DoesNotExist:
            return Response({"error":"don't exist car with this plate"},status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
        





 

