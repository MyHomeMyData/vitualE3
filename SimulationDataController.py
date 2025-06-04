import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class SimulationDataController(BaseHTTPRequestHandler):
    ecus = {}

    def do_GET(self):
        if self.path == "/ecus":
            response = {hex(addr): {"dids": list(ecu[0].keys()), "data": {k: v.decode('utf-8', errors='replace') if isinstance(v, bytes) else v for k, v in ecu[1].items()}} for addr, ecu in self.ecus.items()}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/reset-ecu-simulation-data":
            for ecu in self.ecus.values():
                ecu[1].clear_overlay()

            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(405)
            self.end_headers()


def run(port, ecus):
    SimulationDataController.ecus = ecus

    server_address = ('', port)
    httpd = HTTPServer(server_address, SimulationDataController)

    print(f"Starting web server on port {port}...")
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    print("Web server started.")

    return httpd