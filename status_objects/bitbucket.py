
from status_objects.generic_status import GenericStatus


class Bitbucket(GenericStatus):
    def __init__(self):
        link = 'https://bitbucket.status.atlassian.com/api/v2/status.json'
        super().__init__("Bitbucket", link)

        response_as_dict = self.get_status_endpoint_response()

        found_status = response_as_dict['status']['indicator']
        if found_status == 'none':
            self.set_status_ok()
        else:
            self.set_status_incident()
        self.detail = "detail"


