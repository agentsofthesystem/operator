import sys
import validators

from operator_client.v1.urls import AppUrls
from operator_client.v1.access import AccessClient
from operator_client.v1.architect import ArchitectClient
from operator_client.v1.app import BaseAppClient
from operator_client.v1.game import SupportedGameClient
from operator_client.v1.steam import SteamGameClient


class Operator:
    def __init__(
        self,
        hostname: str,
        port: int = None,
        verbose: bool = False,
        timeout: int = 5,  # seconds
        token: str = None,
        certificate: str = None,
    ) -> None:
        self._host = hostname if port is None else f"{hostname}:{port}"

        # Url validator blocks the two localhost conditions, so explicitly passing them.
        if hostname == "http://localhost" or hostname == "https://localhost":
            pass  # This is allowed.
        elif not validators.url(self._host):
            print(f"Client: Error! Unformatted Url: {self._host}")
            sys.exit(1)

        urls = AppUrls(self._host)
        self._urls = urls

        self.access = AccessClient(
            urls, verbose, token=token, certificate=certificate, timeout=timeout
        )
        self.steam = SteamGameClient(
            urls, verbose, token=token, certificate=certificate, timeout=timeout
        )
        self.game = SupportedGameClient(
            urls, verbose, token=token, certificate=certificate, timeout=timeout
        )
        self.app = BaseAppClient(
            urls, verbose, token=token, certificate=certificate, timeout=timeout
        )
        self.architect = ArchitectClient(
            urls, verbose, token=token, certificate=certificate, timeout=timeout
        )
