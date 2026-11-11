import httpx

class SpotifyClient:
    def __init__(self, api_token):
        self._api_token = api_token
        self.headers = {"Authorization": f"Bearer {api_token}"}
    
    