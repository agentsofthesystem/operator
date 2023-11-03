import sys
import validators

from operator_client.v1.urls import AppUrls
from operator_client.v1.access import AccessClient
from operator_client.v1.app import BaseAppClient
from operator_client.v1.executable import GenericExecutableClient
from operator_client.v1.game import SupportedGameClient
from operator_client.v1.steam import SteamGameClient


class Operator:
    def __init__(self, hostname, port=None, verbose=False, token=None) -> None:
        self._host = hostname if port is None else f"{hostname}:{port}"

        if not validators.url(self._host):
            print(f"Client: Error! Unformatted Url: {self._host}")
            sys.exit(1)

        urls = AppUrls(self._host)
        self._urls = urls

        self.access = AccessClient(urls, verbose, token=token)
        self.steam = SteamGameClient(urls, verbose, token=token)
        self.exe = GenericExecutableClient(urls, verbose, token=token)
        self.game = SupportedGameClient(urls, verbose, token=token)
        self.app = BaseAppClient(urls, verbose, token=token)
