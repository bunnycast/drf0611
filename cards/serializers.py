from rest_framework.serializers import ModelSerializer
from cards import models


class CardSerializer(ModelSerializer):
    class Meta:
        model = models.Cards
        fields = ('id', 'user', 'title', 'contents,', 'created_at', 'is_reported', 'color',)
