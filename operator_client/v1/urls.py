class AppUrls:
    BASE_URL = "{host_name}/{api_version}"

    def __init__(self, host: str) -> None:
        self._host = host
        self._api_version = "v1"

    @property
    def base_url(self) -> str:
        return self.BASE_URL.format(host_name=self._host, api_version=self._api_version)

    ###############################################################################
    ###############################################################################
    # Base App Specific Urls
    ###############################################################################
    ###############################################################################

    def get_settings_url(self) -> str:
        return f"{self.base_url}/settings"

    def get_settings_by_id_url(self, setting_id: int) -> str:
        return f"{self.base_url}/settings/{setting_id}"

    def get_settings_by_name_url(self, setting_name: str) -> str:
        return f"{self.base_url}/settings/name/{setting_name}"

    def get_thread_alive_url(self, thread_ident: int) -> str:
        return f"{self.base_url}/thread/status/{thread_ident}"

    def get_gui_initialization_data_url(self) -> str:
        return f"{self.base_url}/gui/startup"

    ###############################################################################
    ###############################################################################
    # Architect Specific Urls
    ###############################################################################
    ###############################################################################

    def get_health_url(self) -> str:
        return f"{self.base_url}/architect/health"

    def get_secure_health_url(self) -> str:
        return f"{self.base_url}/architect/health/secure"

    def get_agent_info_url(self) -> str:
        return f"{self.base_url}/architect/agent/info"

    ###############################################################################
    ###############################################################################
    # Steam App Urls
    ###############################################################################
    ###############################################################################

    def get_install_url(self) -> str:
        return f"{self.base_url}/steam/app/install"

    def get_remove_url(self) -> str:
        return f"{self.base_url}/steam/app/remove"

    def get_update_url(self) -> str:
        return f"{self.base_url}/steam/app/update"

    def get_app_info_url(self) -> str:
        return f"{self.base_url}/steam/app/info"

    def get_app_build_id_url(self) -> str:
        return f"{self.base_url}/steam/app/build/id"

    ###############################################################################
    ###############################################################################
    # Supported Game Related Urls
    ###############################################################################
    ###############################################################################

    def get_all_games_url(self) -> str:
        return f"{self.base_url}/games"

    def get_game_by_name_url(self, game_name) -> str:
        return f"{self.base_url}/game/{game_name}"

    def get_update_game_url(self, game_id) -> str:
        return f"{self.base_url}/game/{game_id}"

    def get_game_status_by_name_url(self, game_name) -> str:
        return f"{self.base_url}/game/status/{game_name}"

    def get_games_args_url(self, name) -> str:
        return f"{self.base_url}/games/{name}/arguments"

    def get_games_schmea_url(self) -> str:
        return f"{self.base_url}/games/schema"

    def get_game_startup_url(self, game_name) -> str:
        return f"{self.base_url}/game/startup/{game_name}"

    def get_game_shutdown_url(self, game_name) -> str:
        return f"{self.base_url}/game/shutdown/{game_name}"

    def get_game_uninstall_url(self, game_name) -> str:
        return f"{self.base_url}/game/uninstall/{game_name}"

    def get_game_update_check_url(self, game_id) -> str:
        return f"{self.base_url}/game/update/check/{game_id}"

    def get_arguments_url(self) -> str:
        return f"{self.base_url}/game/arguments"

    def get_argument_by_id_url(self, argument_id: int) -> str:
        return f"{self.base_url}/game/argument/{argument_id}"

    def get_argument_by_name_url(self, game_name, argument_name: str) -> str:
        return f"{self.base_url}/game/{game_name}/argument/{argument_name}"

    ###############################################################################
    ###############################################################################
    # Token/Access Related Urls
    ###############################################################################
    ###############################################################################

    def get_active_tokens(self) -> str:
        return f"{self.base_url}/tokens"

    def get_token_generation_url(self, token_name: str) -> str:
        return f"{self.base_url}/token/generate?token_name={token_name}"

    def get_token_verification_url(self, token_name: str) -> str:
        return f"{self.base_url}/token/verify?token_name={token_name}"

    def get_token_invalidation_url(self, token_name: str) -> str:
        return f"{self.base_url}/token/invalidate?token_name={token_name}"
