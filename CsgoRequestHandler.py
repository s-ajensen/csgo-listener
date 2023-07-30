import socketserver
from http.server import BaseHTTPRequestHandler
import re
import json

import player


class CsgoRequestHandler(BaseHTTPRequestHandler):
    def __init__(self):
        self.isPlaying = False

    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer):
        self.isPlaying = False
        super().__init__(request, client_address, server)

    def __readBody(self) -> dict:
        contentLen = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(contentLen).decode().strip()
        trimmed = re.sub(r"\s+", "", raw, flags=re.UNICODE)
        return json.loads(trimmed)


    def __shouldPlay(self, req):
        mapSection = req["map"]
        roundSection = req["round"]

        return (not ((mapSection["phase"] == "live") and (mapSection["mode"] == "competitive"))) or (roundSection["phase"] == "freezetime")

    def __handle(self):
        req = self.__readBody()
        print("req: %s" % req)

        try:
            if self.__shouldPlay(req):
                player.play()
            else:
                player.pause()
        except:
            player.play()


    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.__handle()
