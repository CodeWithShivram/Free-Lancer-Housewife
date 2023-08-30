
from rest_framework import serializers

# as serializers module is in rest_framework package therefore we need to import 

class enquiry_tableSerializer(serializers.Serializer):
    # Rememer serializers.Serializer - S is capital of Serializer
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=10)
    

