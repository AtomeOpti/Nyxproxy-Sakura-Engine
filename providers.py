class ProviderManager:
    """
    Proxy provider endpoint manager.
    """
    def __init__(self):
        # Demo endpoint list (real sources hidden)
        self._endpoints = [
            "https://api.nyxproxy.local/v1/feed_demo",
        ]

    def get_active_providers(self):
        return self._endpoints