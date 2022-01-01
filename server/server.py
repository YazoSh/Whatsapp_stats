import json
import socketserver
from http.server import *

from helpers import *

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = sendData('path', "." + self.path)
        if data:
            data = json.dumps(data)

            endl = "\r\n"

            resp = "HTTP/1.1 200 OK" + endl
            resp += "Content-Type: application/json"    + endl
            resp += f"Content-Length: {len(data)}"      + endl
            resp += "Access-Control-Allow-Origin: *"    + endl
            resp += endl
            resp += data + endl

            self.wfile.write(bytes(resp, 'utf-8'))
        else:
            print(self.rfile.read(100))
            self.send_response(404)

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        data = sendData('raw', self.rfile.read(content_len).decode('utf-8'))
        if data:
            data = json.dumps(data)

            endl = "\r\n"

            resp = "HTTP/1.1 200 OK" + endl
            resp += "Content-Type: application/json"    + endl
            resp += f"Content-Length: {len(data)}"      + endl
            resp += "Access-Control-Allow-Origin: *"    + endl
            resp += endl
            resp += data + endl

            self.wfile.write(bytes(resp, 'utf-8'))
        pass



def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run(HTTPServer, MyHandler)
