from http.server import HTTPServer
from CsgoRequestHandler import CsgoRequestHandler
from pprint import pprint

hostName = "localhost"
serverPort = 3000

if __name__ == '__main__':
    server = HTTPServer((hostName, serverPort), CsgoRequestHandler)
    pprint("Server started on http://%s:%s" % (hostName, serverPort))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    pprint("Server stopped.")
