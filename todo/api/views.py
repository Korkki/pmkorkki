from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from todo.api.serializers import ItemSerializer
from todo.models import Item


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
