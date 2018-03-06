from rest_framework import serializers

from ejemplo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = 'id', 'text', 'done'