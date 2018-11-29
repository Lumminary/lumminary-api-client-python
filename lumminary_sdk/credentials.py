import os
import json

class Credentials:
    API_ENDPOINT = "https://api.lumminary.com/v1"
    ROLE_APP = "role_product"

    def __init__(self, login = None, api_key = None, host = None, role = None):
        if host is None:
            host = Credentials.API_ENDPOINT
        if role is None:
            role = Credentials.ROLE_APP

        self.login = login
        self.api_key = api_key
        self.host = host
        self.role = role

    def load_json_credentials(self, credentialsFilePath):
        with open(credentialsFilePath, "r") as credentialsFile:
            config = json.load(credentialsFile)

        credentialsExpected = ["login", "api_key", "role", "host"]
        for credentialsAttribute in credentialsExpected:
            if credentialsAttribute in config:
                setattr(self, credentialsAttribute, config[credentialsAttribute])
            else:
                if getattr(self, credentialsAttribute, None) is None:
                    raise ValueError("Expecting config attribute {0} to be either explicitly defined or present in config file. None found".format(
                        credentialsAttribute
                    ))
