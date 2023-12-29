from operator_client.common.base_client import BaseClient, RequestTypes
from operator_client.v1.urls import AppUrls


class ArchitectClient(BaseClient):
    def __init__(self, urls: AppUrls, verbose: bool, token: str = None) -> None:
        super(ArchitectClient, self).__init__(urls, verbose, token)

    def get_health(self, secure_version=False):
        if secure_version:
            get_url = self._urls.get_secure_health_url()
        else:
            get_url = self._urls.get_health_url()

        if self._verbose:
            print("Getting Health:")
            print(f"Get Url: {get_url}")

        response = self.make_request(RequestTypes.GET, get_url)
        self.handle_response(response)

        if response.status_code == 200:
            output = response.json()
        else:
            output = None

        return output

    def get_agent_info(self):
        get_url = self._urls.get_agent_info_url()

        if self._verbose:
            print("Getting Health:")
            print(f"Get Url: {get_url}")

        response = self.make_request(RequestTypes.GET, get_url)
        self.handle_response(response)

        if response.status_code == 200:
            output = response.json()
        else:
            output = None

        return output
