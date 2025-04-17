from drf_spectacular.utils import OpenApiExample


CREATE_FUND_REQUEST_PAYLOAD = OpenApiExample(
    name="Sample Request Body",
    value={
        "name": "Funds ABC",
        "managerName": "Test Manager",
        "description": "Test Description fields",
        "netAssetValue": "30.35",
        "dateCreation": "2025-04-18",
        "performance": "25.11",
    },
    request_only=True,
)

CREATE_FUND_RESPONSE_PAYLOAD = OpenApiExample(
    name="Sample Response Body",
    value={
        "id": 1,
        "name": "Funds ABC",
        "managerName": "Test Manager",
        "description": "Test Description fields",
        "netAssetValue": "30.35",
        "dateCreation": "2025-04-18",
        "performance": "25.11",
    },
    response_only=True,
)

UPDATE_FUND_REQUEST_PAYLOAD = OpenApiExample(
    name="Sample Request Body",
    value={
        "name": "Updated Funds ABC",
        "managerName": "Updated Test Manager",
        "description": "Updated Test Description fields",
        "netAssetValue": "11.11",
        "dateCreation": "2025-04-18",
        "performance": "11.11",
    },
    request_only=True,
)

UPDATE_FUND_RESPONSE_PAYLOAD = OpenApiExample(
    name="Sample Response Body",
    value={
        "id": 1,
        "name": "Updated Funds ABC",
        "managerName": "Updated Test Manager",
        "description": "Updated Test Description fields",
        "netAssetValue": "11.11",
        "dateCreation": "2025-04-18",
        "performance": "11.11",
    },
    response_only=True,
)

PARTIAL_UPDATE_FUND_PERFORMANCE_REQUEST_PAYLOAD = OpenApiExample(
    name="Sample Request Body",
    value={
        "performance": "99.99",
    },
    request_only=True,
)

PARTIAL_UPDATE_FUND_PERFORMANCE_RESPONSE_PAYLOAD = OpenApiExample(
    name="Sample Response Body",
    value={
        "id": 1,
        "name": "Updated Funds ABC",
        "managerName": "Updated Test Manager",
        "description": "Updated Test Description fields",
        "netAssetValue": "11.11",
        "dateCreation": "2025-04-18",
        "performance": "99.99",
    },
    response_only=True,
)

PARTIAL_UPDATE_FUND_REQUEST_PAYLOAD = OpenApiExample(
    name="Sample Request Body",
    value={
        "managerName": "Partial Update Manager Name",
    },
    request_only=True,
)

PARTIAL_UPDATE_FUND_RESPONSE_PAYLOAD = OpenApiExample(
    name="Sample Response Body",
    value={
        "id": 1,
        "name": "Updated Funds ABC",
        "managerName": "Partial Update Manager Name",
        "description": "Updated Test Description fields",
        "netAssetValue": "11.11",
        "dateCreation": "2025-04-18",
        "performance": "11.11",
    },
    response_only=True,
)
