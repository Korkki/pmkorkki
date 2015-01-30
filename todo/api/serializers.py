from rest_framework.serializers import ModelSerializer
from todo.models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
