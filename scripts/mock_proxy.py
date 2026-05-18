import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
# Original API Key found in history as fallback for restricted ADC projects
FALLBACK_API_KEY = "AIzaSyB5X3MDs1UB6x3BLjAuxgjNwKqCKL85kG4"

def get_api_key():
    """Retrieves the API Key from environment variables."""
    return os.getenv("GOOGLE_API_KEY")

class LobsterTrapMock(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))

        # Log Lobster Trap Metadata
        lt_metadata = payload.get("extra_body", {}).get("_lobstertrap") or payload.get("_lobstertrap")
        print(f"\n[LOBSTER TRAP PROXY] Intercepted Request from: {self.client_address}")
        if lt_metadata:
            print(f"[LOBSTER TRAP PROXY] Governance Metadata: {json.dumps(lt_metadata, indent=2)}")
        else:
            print("[LOBSTER TRAP PROXY] WARNING: No _lobstertrap metadata found!")

        # Clean payload for Gemini (remove extra_body and _lobstertrap)
        if "extra_body" in payload:
            del payload["extra_body"]
        if "_lobstertrap" in payload:
            del payload["_lobstertrap"]

        # Get API Key
        api_key = get_api_key()
        
        # Prepare headers
        headers = {"Content-Type": "application/json"}
        
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
            print(f"[LOBSTER TRAP PROXY] Forwarding with API Key")
        else:
            print("[LOBSTER TRAP PROXY] ERROR: GOOGLE_API_KEY missing in environment!")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"GOOGLE_API_KEY missing")
            return

        req = urllib.request.Request(
            BACKEND_URL,
            data=json.dumps(payload).encode('utf-8'),
            headers=headers,
            method="POST"
        )

        try:
            with urllib.request.urlopen(req) as response:
                res_data = response.read()
                self.send_response(response.status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(res_data)
                print(f"[LOBSTER TRAP PROXY] Request Forwarded Successfully (Status: {response.status})")
        except urllib.error.HTTPError as e:
            print(f"[LOBSTER TRAP PROXY] Error from Backend: {e.code} {e.reason}")
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(e.read())

def run(server_class=HTTPServer, handler_class=LobsterTrapMock, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting Lobster Trap Mock on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
