
from status_objects.generic_status import GenericStatus


# f = open("example.txt", "r")
# text = f.read()
# response_as_dict = json.loads(text)
# f.close()

class Slack(GenericStatus):
    def __init__(self):
        link = 'https://status.slack.com/api/v2.0.0/current'
        super().__init__("Slack", link)
        response_as_dict = self.get_status_endpoint_response()

        found_status = response_as_dict['status']
        if found_status == 'ok':
            self.set_status_ok()
        else:
            self.set_status_incident()
        self.detail = "detail"
