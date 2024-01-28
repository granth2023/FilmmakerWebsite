from rest_framework import serializers
from .models import myapp 

class Projectserializer(serializers.ModelSerializer):
    class Meta: 
        model = myapp 
        fields ='__all__'