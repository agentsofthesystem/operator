from operator_client.common.base_client import BaseClient, RequestTypes
from operator_client.v1.urls import AppUrls


class SteamGameClient(BaseClient):
    def __init__(
        self,
        urls: AppUrls,
        verbose: bool,
        token: str = None,
        certificate: str = None,
        timeout: int = 5,
    ) -> None:
        super(SteamGameClient, self).__init__(
            urls, verbose, token, certificate, timeout
        )

    def install_steam_app(
        self,
        steam_install_path,
        steam_id,
        install_dir,
        user="anonymous",
        password=None,
        input_args=None,
    ) -> bool:
        post_url = self._urls.get_install_url()

        if self._verbose:
            print("Installing Application:")
            print(f"Post Url: {post_url}")

        payload = {
            "steam_install_path": steam_install_path,
            "steam_id": steam_id,
            "install_dir": install_dir,
            "user": user,
            "password": password,
        }

        if input_args:
            payload.update(input_args)

        if self._verbose:
            print("Installing Application:")
            print(f"Post Url: {post_url}")

        response = self.make_request(RequestTypes.POST, post_url, payload=payload)
        self.handle_response(response)

        thread_ident = None

        if response.status_code == 200:
            json_data = response.json()
            thread_ident = json_data["thread_ident"]

        return thread_ident

    def update_steam_app(
        self, steam_install_path, steam_id, install_dir, user="anonymous", password=None
    ) -> bool:
        post_url = self._urls.get_update_url()

        payload = {
            "steam_install_path": steam_install_path,
            "steam_id": steam_id,
            "install_dir": install_dir,
            "user": user,
            "password": password,
        }

        if self._verbose:
            print("Updating Application:")
            print(f"Post Url: {post_url}")

        response = self.make_request(RequestTypes.POST, post_url, payload=payload)
        self.handle_response(response)

        thread_ident = None

        if response.status_code == 200:
            json_data = response.json()
            thread_ident = json_data["thread_ident"]

        return thread_ident

    def get_steam_app_build_id(
        self, steam_install_path, game_install_path, steam_id
    ) -> bool:
        post_url = self._urls.get_app_build_id_url()

        payload = {
            "steam_install_path": steam_install_path,
            "game_install_path": game_install_path,
            "steam_id": steam_id,
        }

        if self._verbose:
            print("Getting Steam Application ID From Manifest File:")
            print(f"Post Url: {post_url}")

        response = self.make_request(RequestTypes.POST, post_url, payload=payload)
        self.handle_response(response)

        json_data = None

        if response.status_code == 200:
            json_data = response.json()

        return json_data

    def get_steam_app_info(
        self, steam_install_path, steam_id, user="anonymous", password=None
    ) -> bool:
        post_url = self._urls.get_app_info_url()

        payload = {
            "steam_install_path": steam_install_path,
            "steam_id": steam_id,
            "user": user,
            "password": password,
        }

        if self._verbose:
            print("Getting Steam Application Info:")
            print(f"Post Url: {post_url}")

        response = self.make_request(RequestTypes.POST, post_url, payload=payload)
        self.handle_response(response)

        json_data = None

        if response.status_code == 200:
            json_data = response.json()

        return json_data

    def remove_steam_app(self):
        post_url = self._urls.get_remove_url()

        if self._verbose:
            print("Removing Application:")
            print(f"Post Url: {post_url}")

        response = self.make_request(RequestTypes.POST, post_url)
        self.handle_response(response)
