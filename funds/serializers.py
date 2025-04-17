from rest_framework import serializers

from .models import Fund


class FundSerializer(serializers.ModelSerializer):
    """
    Serializer for Fund's data model.
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Fund
        fields = "__all__"
