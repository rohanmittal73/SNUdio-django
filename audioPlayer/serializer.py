from rest_framework import serializers
from .models import AudioFile


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioFile
        fields = ('title', 'description', 'image', 'audio')
