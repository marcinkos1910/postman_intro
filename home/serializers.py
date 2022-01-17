from rest_framework import serializers

from home.models import OurModel


class OurModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurModel
        fields = '__all__'
