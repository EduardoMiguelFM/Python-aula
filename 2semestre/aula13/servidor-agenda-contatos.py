from http.server import BaseHTTPRequestHandler, HTTPServer
import json

lista=[]


class MeuRequestHandler(BaseHTTPRequestHandler):
    def do_GET (self):
        print("Cliente se conectou e pediu um GET")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
    
        texto_json = jsn.dmps(lista)
        self.wfile.write(texto_json.encode('utf-8'))

    def do_POST (self):
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()

        length = int(self.headers.get(''))

print("Iniciando o servidor")
servidor = HTTPServer (('127.0.0.1', 80), MeuRequestHandler)
print("Aguardando servidor")
servidor.handle_request()
