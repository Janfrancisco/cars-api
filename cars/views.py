from rest_framework import viewsets
from cars.filters import BrandFilterClass, CarFilterClass
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer, CarNamesModelSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    rql_filter_class = BrandFilterClass


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    rql_filter_class = CarFilterClass

    # Se for listar ou recuperar carros, retorna com o nome do proprietário e a marca do carro ao invés dos 'ids'
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarNamesModelSerializer
        return CarModelSerializer
