import requests 
from django.conf import settings 

class ThirdPartyAPIClient:
    base_url = 'http://www.omdbapi.com'
    headers = {'Authorization': f'Bearer {settings.OMDB_API_KEY}'}
    
    @staticmethod
    def get_resource(resource_id): 
        response = requests.get(f'{ThirdPartyAPIClient.base_url}/resource/{resource_id}', headers=ThirdPartyAPIClient.headers)
        response.raise_for_status()
        return response.json()