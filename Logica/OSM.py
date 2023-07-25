
import requests

class Api_osm:
    def __init__(self, region):
        self.region=region
        self.response=[]

    def get_crosswalks(self):

        # REQUEST URL
        if self.region != []:
            base_api_osm = 'https://overpass-api.de/api/'
            node_query = '["crossing"~"marked"]'
            lat_min, lon_min, lat_max, lon_max = self.region
            bbox_str = f'{lat_min},{lon_min},{lat_max},{lon_max}'
            params = f'interpreter?data=[out:json];node{node_query}({bbox_str});out body;'
            request_url = base_api_osm + params
            self.response = requests.get(request_url).json()

        else:
            self.response={'elements':[]}
        return self.response