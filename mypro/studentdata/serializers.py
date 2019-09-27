from rest_framework import serializers
from studentdata.models import det

class detSerializer(serializers.ModelSerializer):
    class Meta:
        model= det
        fields= ['name','email','phno']