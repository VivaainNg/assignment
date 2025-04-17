from rest_framework import status
from django.urls import reverse

from model_bakery import baker
from rest_framework.status import is_success
from rest_framework.test import APITestCase

from .models import Fund


class FundViewSetTestCase(APITestCase):
    """
    Class for setting up unit tests for Fund's endpoints.
    """

    @classmethod
    def setUpTestData(cls):
        cls.fund = baker.make(
            Fund,
            name="Test Name",
            manager_name="Test Manager Name",
            description="Test Description",
            net_asset_value="1530.35",
            date_creation="2025-01-20",
            performance="77.50",
        )

    def setUp(self):
        self.list_endpoint = reverse("funds:funds-list")

    def test_list(self):
        """
        Test GET request to retrieve a list of all Fund objects.
        """
        response = self.client.get(self.list_endpoint)
        self.assertTrue(is_success(response.status_code))
        self.assertTrue(response.json())

    def test_get(self):
        """
        Test GET request to retrieve a single Fund object via its ID/pk.
        """
        fund = Fund.objects.first()
        response = self.client.get(reverse("funds:funds-detail", args=[fund.pk]))
        json_data = response.json()

        self.assertTrue(is_success(response.status_code))
        self.assertEqual(json_data["name"], "Test Name")
        self.assertEqual(json_data["managerName"], "Test Manager Name")
        self.assertEqual(json_data["description"], "Test Description")
        self.assertEqual(json_data["netAssetValue"], "1530.35")
        self.assertEqual(json_data["dateCreation"], "2025-01-20")
        self.assertEqual(json_data["performance"], "77.50")

    def test_post(self):
        """
        Test POST request to create a new Fund object.
        """
        payload = {
            "name": "Funds ABC",
            "managerName": "Manager ABC",
            "description": "Description ABC",
            "netAssetValue": "222.22",
            "dateCreation": "2025-04-18",
            "performance": "20.20",
        }
        response = self.client.post(self.list_endpoint, data=payload, format="json")
        json_data = response.json()

        self.assertTrue(is_success(response.status_code))
        self.assertEqual(json_data["name"], "Funds ABC")
        self.assertEqual(json_data["managerName"], "Manager ABC")
        self.assertEqual(json_data["description"], "Description ABC")
        self.assertEqual(json_data["netAssetValue"], "222.22")
        self.assertEqual(json_data["dateCreation"], "2025-04-18")
        self.assertEqual(json_data["performance"], "20.20")

    def test_put(self):
        """
        Test PUT request to do a full update based on a Fund's ID.
        """
        fund = Fund.objects.first()
        put_url = reverse("funds:funds-detail", args=[fund.pk])
        put_payload = {
            "name": "Funds Full Updated",
            "managerName": "Manager Full Updated",
            "description": "Description Full Updated",
            "netAssetValue": "222.22",
            "dateCreation": "2025-04-15",
            "performance": "33.33",
        }
        response = self.client.put(put_url, data=put_payload, format="json")
        json_data = response.json()

        self.assertTrue(is_success(response.status_code))
        self.assertEqual(json_data["name"], "Funds Full Updated")
        self.assertEqual(json_data["managerName"], "Manager Full Updated")
        self.assertEqual(json_data["description"], "Description Full Updated")
        self.assertEqual(json_data["netAssetValue"], "222.22")
        self.assertEqual(json_data["dateCreation"], "2025-04-15")
        self.assertEqual(json_data["performance"], "33.33")

    def test_patch_update_performance(self):
        """
        Test PATCH request to update only on Fund's performance field based on a Fund's ID.
        """
        fund = Fund.objects.first()
        patch_url = reverse("funds:funds-update-performance", args=[fund.pk])
        patched_payload = {
            "performance": "100.00",
        }
        response = self.client.patch(patch_url, data=patched_payload, format="json")
        json_data = response.json()

        self.assertTrue(is_success(response.status_code))
        self.assertEqual(json_data["performance"], "100.00")

    def test_patch(self):
        """
        Test PATCH request to update on any of Fund's field based on a Fund's ID.
        """
        fund = Fund.objects.first()
        patch_url = reverse("funds:funds-detail", args=[fund.pk])
        patched_payload = {
            "name": "PATCH FUNDS NAME",
        }
        response = self.client.patch(patch_url, data=patched_payload, format="json")
        json_data = response.json()

        self.assertTrue(is_success(response.status_code))
        self.assertEqual(json_data["name"], "PATCH FUNDS NAME")

    def test_delete(self):
        """
        Test DELETE request to delete an existing Fund based on it's ID.
        """

        # Before deletes a Fund
        json_data = self.client.get(self.list_endpoint).json()
        self.assertEqual(len(json_data["results"]), 1)

        fund = Fund.objects.first()
        delete_url = reverse("funds:funds-detail", args=[fund.pk])
        response = self.client.delete(delete_url)
        json_data = self.client.get(self.list_endpoint).json()

        # After deletes a Fund
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(json_data["results"]), 0)
