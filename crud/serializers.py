from rest_framework import serializers
from .models import *

class BooklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booklist
        fields = '__all__'