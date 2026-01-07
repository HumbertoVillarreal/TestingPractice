from rest_framework import serializers
from .models import Factory, Line, Machine

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields  ="__all__"
        read_only_fields = ("created_by", "created_at")


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields  ="__all__"
        read_only_fields = ("created_by", "created_at")


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields  ="__all__"
        read_only_fields = ("created_by", "created_at")