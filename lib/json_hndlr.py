# boilerplate to deal with json files
# in case later we need to switch to a proper db
# keep this biz separated out over nyah

import json

class jsonP(object):

    def __init__(self, p):
        self.p = p

    # how we'll open a json file
    def open_json(self):
        with open(self.p) as p_file:
           p_json = json.load(p_file)
            
    # how we'll close a json file
    def close_json(self):
       pass 
