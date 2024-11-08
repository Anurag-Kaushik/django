# serializers.py
from rest_framework import serializers
from users.models import CSVData

class CsvDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVData
        fields = ['id', 'name', 'address']
