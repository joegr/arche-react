from rest_framework import serializers
from .models import Deed

class DeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deed
        fields = ('id', 'title', 'detail', 'done')
