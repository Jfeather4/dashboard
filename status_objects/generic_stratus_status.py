import datetime
import json

import requests


class GenericStatus:

    def __init__(self, given_name, given_link):
        self.name = given_name
        self.link = given_link
        self.timestamp = datetime.datetime.now()
        # "ok" is considered normal, all else are alerts
        self.status = None
        self.detail = None
        self.raw = None

    def get_status_endpoint_response(self):
        print("Getting status for "+self.name+"...")
        response = requests.get(self.link)
        response_as_dict = json.loads(response.text)
        self.raw = response_as_dict
        return response_as_dict

    def set_status_ok(self):
        self.status = 'ok'

    def set_status_incident(self):
        self.status = 'incident'
