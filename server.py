import falcon
import json
from wsgiref import simple_server


class ServerAPI:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({"Server_status": "Online"})

if __name__ == "__main__":

    app = falcon.API()
    instance = ServerAPI()
    app.add_route('/status', instance)
    httpd = simple_server.make_server('127.0.0.1', 35005, app)
    httpd.serve_forever()
