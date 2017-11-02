from rest_framework import serializers

from .models import Categories, Items


class ItemsSerializer(serializers.ModelSerializer):
    """Serializer model."""

    class Meta:
        """Serializer meta model."""

        model = Items
        fields = ('ID', 'Title', 'Description',
                  'User', 'CreatedAt', 'ChangedAt')


class CategoriesSerializer(serializers.ModelSerializer):
    """Serializer model."""

    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        """Serializer meta model."""

        model = Categories
        fields = ('ID', 'Name', 'items')
