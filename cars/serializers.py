from rest_framework import serializers

from cars.models import Brand, Car

CAR_FIELDS = ('id', 'model', 'brand', 'factory_year', 'model_year', 'color', 'owner', 'description', 'created_at', 'updated_at',)


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = CAR_FIELDS


class CarNamesModelSerializer(serializers.ModelSerializer):
    """
        Retorna o nome do proprietário e a marca do carro ao invés de retornar as suas 'ids'
    """
    brand = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = CAR_FIELDS

    def get_brand(self, obj):
        return obj.brand.name

    def get_owner(self, obj):
        return obj.owner.username
