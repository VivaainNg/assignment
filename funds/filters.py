from django_filters import rest_framework as filters

from funds.models import Fund


class FundFilter(filters.FilterSet):
    """
    The filter set to perform dynamic QuerySet filtering from URL parameters
    based on Fund data model.
    """

    id = filters.NumberFilter()
    date_creation_min = filters.DateFilter(
        field_name="date_creation", lookup_expr="gte"
    )
    date_creation_max = filters.DateFilter(
        field_name="date_creation", lookup_expr="lte"
    )
    performance_min = filters.NumberFilter(field_name="performance", lookup_expr="gte")
    performance_max = filters.NumberFilter(field_name="performance", lookup_expr="lte")

    class Meta:
        model = Fund
        fields = [
            "id",
            "date_creation_min",
            "date_creation_max",
            "performance_min",
            "performance_max",
        ]
