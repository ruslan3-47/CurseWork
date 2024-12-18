from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
class UserDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = "__all__"

    def get_name(self, obj):
        return f'{obj.first_name} - {obj.last_name}'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"