import requests
import os
import pathlib

import config


class Unload:

    def __init__(self):

        configurations = config.Config()

        self.source = configurations.source
        self.uri = configurations.uri

    def directory(self):
        
        directory_ = pathlib.Path(self.uri).parent

        if not os.path.exists(directory_):
            os.makedirs(directory_)

    def request(self):

        try:
            req = requests.get(self.source)
        except OSError as err:
            raise Exception(err.strerror) from err

        return req

    def exc(self):
        
        self.directory()

        with open(self.uri, 'wb') as data:
            data.write(self.request().content)
