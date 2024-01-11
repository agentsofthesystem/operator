import os
import requests
import sys
import tempfile

from operator_client.common import logger
from operator_client.v1.urls import AppUrls
from enum import Enum


class RequestTypes(Enum):
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class FakeResponse(object):
    def __init__(self, status_code) -> None:
        self.status_code = status_code

    def json(self):
        return None


class BaseClient:
    def __init__(
        self,
        urls: AppUrls,
        verbose: bool,
        token: str = None,
        certificate: str = None,
        timeout: int = 5,
    ) -> None:
        self._urls = urls
        self._verbose = verbose
        self._token = token
        self._timeout = timeout  # seconds.

        # In the event the user passed a certificate string.
        self._certificate = certificate if certificate else None

    def handle_response(self, response: requests.Response) -> None:
        if response.status_code == 200:
            print("Request made successfully!")
            if hasattr(response, "json") and self._verbose:
                print("Application Returned Json:")
                print(response.text)
        elif response.status_code == 401:
            print("Authorization Error: Request Made, but missing bearer token.")
        elif response.status_code == 403:
            print("Authorization Error: Token is not authorized.")
        elif response.status_code == 404:
            print("Authorization Error: Path Requested does not exist!")
        elif response.status_code == 500:
            print("Error: 500 - Internal Server Error - It's not the client.")
        elif response is None:
            print("Error: Response Object is None.")
        else:
            print(f"Error: Other Response Code: {response.status_code}")
            if self._verbose:
                print(f"    {response.content}")

    def make_request(
        self,
        request_type: RequestTypes,
        request_url: str,
        parameter_list: list = [],
        payload: dict = {},
    ) -> requests.Response:
        if len(parameter_list) > 0:
            for i in range(0, len(parameter_list)):
                if i == 0:
                    request_url += f"?{parameter_list[i]}"
                else:
                    request_url += f"&{parameter_list[i]}"

        if self._verbose:
            logger.info(f"Request URL: {request_url}")

        headers = {}  # Empty by default

        if self._token:
            headers = {
                "Authorization": "Bearer " + self._token,
                "Content-Type": "application/json",
            }

        cert_file_name = False  # Default to false for http.

        # If there is a certificate, create a temp file and write to it.
        if self._certificate:
            cert_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
            cert_file.write(self._certificate)
            cert_file.seek(0)
            cert_file_name = cert_file.name

        try:
            if request_type == RequestTypes.GET:
                response = requests.get(
                    request_url,
                    headers=headers,
                    timeout=self._timeout,
                    verify=cert_file_name,
                )
            elif request_type == RequestTypes.POST:
                response = requests.post(
                    request_url,
                    json=payload,
                    headers=headers,
                    timeout=self._timeout,
                    verify=cert_file_name,
                )
            elif request_type == RequestTypes.PATCH:
                response = requests.patch(
                    request_url,
                    json=payload,
                    headers=headers,
                    timeout=self._timeout,
                    verify=cert_file_name,
                )
            elif request_type == RequestTypes.DELETE:
                response = requests.delete(
                    request_url,
                    headers=headers,
                    timeout=self._timeout,
                    verify=cert_file_name,
                )
            else:
                print(
                    "BaseClient: make_request: Error! - Unsupported request type! Exiting..."
                )
                sys.exit(1)

        except Exception as error:
            logger.debug("Request Error. Responding with a fake response object.")
            logger.debug(error)
            return FakeResponse(500)
        finally:
            # Eliminate remainder of temp file if it existed in the first place.
            if self._certificate:
                cert_file.close()
                os.unlink(cert_file.name)

        return response
