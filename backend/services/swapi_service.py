import requests
from utils.logger_service import LoggerService

class SwapiService:
    BASE_URL = "https://swapi.dev/api"

    def __init__(self):
        self.logger = LoggerService()

    def get_people(self):
        url = f"{self.BASE_URL}/people/"
        response = requests.get(url)
        self.logger.log_request("GET", url, response.status_code)
        return response.json()
