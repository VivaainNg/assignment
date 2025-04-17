from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework.decorators import action
from djangorestframework_camel_case.render import (
    CamelCaseBrowsableAPIRenderer,
    CamelCaseJSONRenderer,
)
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from funds.filters import FundFilter
from funds.models import Fund

from .serializers import FundSerializer
from .openapi_schema import (
    CREATE_FUND_REQUEST_PAYLOAD,
    CREATE_FUND_RESPONSE_PAYLOAD,
    UPDATE_FUND_REQUEST_PAYLOAD,
    UPDATE_FUND_RESPONSE_PAYLOAD,
    PARTIAL_UPDATE_FUND_PERFORMANCE_RESPONSE_PAYLOAD,
    PARTIAL_UPDATE_FUND_PERFORMANCE_REQUEST_PAYLOAD,
    PARTIAL_UPDATE_FUND_REQUEST_PAYLOAD,
    PARTIAL_UPDATE_FUND_RESPONSE_PAYLOAD,
)


class FundViewSet(viewsets.ModelViewSet):
    """
    ViewSet class for Fund data model.
    """

    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = [permissions.AllowAny]
    serializer_class = FundSerializer
    queryset = Fund.objects.all()
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    parser_classes = [CamelCaseJSONParser]
    filter_backends = [SearchFilter]
    filterset_class = FundFilter
    search_fields = ["name", "manager_name"]

    @extend_schema(
        summary="Endpoint to retrieve a list of all funds",
        description="Retrieve entire list of available funds",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Endpoint to create a new fund",
        description="Create a new fund based on submitted request payload",
        examples=[
            CREATE_FUND_REQUEST_PAYLOAD,
            CREATE_FUND_RESPONSE_PAYLOAD,
        ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Endpoint to retrieve details of a specific fund using its ID",
        description="Retrieve a specific fund based on given ID in the path variable",
        examples=[
            CREATE_FUND_RESPONSE_PAYLOAD,
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Endpoint to fully update a fund using its ID",
        description="Fully update a fund based on given ID in the path variable & full request payload",
        examples=[
            UPDATE_FUND_REQUEST_PAYLOAD,
            UPDATE_FUND_RESPONSE_PAYLOAD,
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Endpoint to only update the performance of a fund using its ID",
        description="Only update the performance of a fund based on given ID in the path variable",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "performance": {
                        "type": "number",
                        "description": "New performance (As percentage)",
                    }
                },
                "required": ["performance"],
            }
        },
        examples=[
            PARTIAL_UPDATE_FUND_PERFORMANCE_REQUEST_PAYLOAD,
            PARTIAL_UPDATE_FUND_PERFORMANCE_RESPONSE_PAYLOAD,
        ],
    )
    @action(detail=True, methods=["patch"], url_path="update-performance")
    def update_performance(self, request, pk=None):
        """
        Custom actions to only update performance based on given Fund's ID.
        """

        try:
            fund = self.get_object()
        except Fund.DoesNotExist:
            return Response(
                {"detail": "Fund not found."}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            performance = request.data.get("performance")

            if not performance:
                return Response(
                    {"detail": "Performance field is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            fund.performance = performance
            fund.save()

            return Response(
                {
                    "detail": "Performance updated successfully.",
                    "performance": fund.performance,
                },
                status=status.HTTP_200_OK,
            )

    @extend_schema(
        summary="Endpoint to partially update a fund using its ID",
        description="Partially update a specific fund based on given ID in the path variable",
        examples=[
            PARTIAL_UPDATE_FUND_REQUEST_PAYLOAD,
            PARTIAL_UPDATE_FUND_RESPONSE_PAYLOAD,
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Endpoint to delete a fund using its ID",
        description="Delete a specific fund based on given ID in the path variable",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
