import web
import app
import json


class Error:
    def GET(self):
        dic={}
        dic['error']="error"
        return json.dumps(dic)
            
            