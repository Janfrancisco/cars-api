from rest_framework import viewsets
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer, CarNamesModelSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarNamesModelSerializer
        return CarModelSerializer
