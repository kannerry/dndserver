from http.server import BaseHTTPRequestHandler, HTTPServer
import time

json_str = "{\"ipAddress\":\"127.0.0.1\",\"port\":13337}"
httpHost = "127.0.0.1" #
httpPort = 8080 # move all this to config

class HelloWorld(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json_str.encode(encoding='utf_8')) 

if __name__ == "__main__":        
    webServer = HTTPServer((httpHost, httpPort), HelloWorld)
    print("HelloWorld Server started on: %s:%s" % (httpHost, httpPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()