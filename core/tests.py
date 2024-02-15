from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Account, Destination
import json
from requests_mock import Mocker

# import logging
# logger = logging.getLogger(__name__)

class IncomingDataAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.account = Account.objects.create(
            email="test@example.com",
            account_name="Test Account",
            website="https://www.example.com",
        )
        self.destination = Destination.objects.create(
            account=self.account,
            url="https://api.example.com/endpoint",
            http_method="POST",
            headers={"Content-Type": "application/json"},
        )

    def test_incoming_data_post_success(self):
        data = {"key": "value"}
        url = reverse("incoming_data")

        with Mocker() as m:
            m.post(self.destination.url, json=data, status_code=200)

            response = self.client.post(
                url, json.dumps(data), content_type="application/json", HTTP_CL_X_TOKEN=self.account.app_secret_token
            )

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json(), {"success": "Data sent successfully"})
            self.assertEqual(m.call_count, 1)  # Assert mock called once

    # def test_incoming_data_post_destination_error(self):
    #     data = {"key": "value"}
    #     url = reverse("incoming_data")

    #     with Mocker() as m:
    #         m.post(self.destination.url, json=data, status_code=500)

    #         response = self.client.post(
    #             url, json.dumps(data), content_type="application/json", HTTP_CL_X_TOKEN=self.account.app_secret_token
    #         )

    #         self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    #         # Add assertion for appropriate error message in response

    # def test_incoming_data_post_invalid_url(self):
    #     data = {"key": "value"}
    #     url = reverse("incoming_data")

    #     with Mocker() as m:
    #         # No mock needed, as the request won't actually reach the destination
    #         invalid_url = "https://invalid-url.com"  # Simulate an invalid URL
    #         self.destination.url = invalid_url

    #         response = self.client.post(
    #             url, json.dumps(data), content_type="application/json", HTTP_CL_X_TOKEN=self.account.app_secret_token
    #         )

    #         self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    #         # Add assertion for appropriate error message in response
