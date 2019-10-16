import http.server
import socketserver
import mt940
import logging
import json

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    def _response_400(self, msg):
        self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.send_header("Content-length", len(msg))
        self.end_headers()

        self.wfile.write(msg.encode(encoding='utf_8'))

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s", str(self.path), str(self.headers))
        message = ""
        message += "<html><body>Hello to mt940 Service.</body></html>"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("Content-length", len(message))
        self.end_headers()

        self.wfile.write(message.encode(encoding='utf_8'))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])

        if content_length <= 1:
            self._response_400('BODY is empty.')
            return

        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        transactions = mt940.parse(post_data)
        message = json.dumps(transactions, cls=mt940.JSONEncoder)

        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.send_header("Content-length", len(message))
        self.end_headers()

        self.wfile.write(message.encode(encoding='utf_8'))
        return


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    logging.basicConfig(level=logging.INFO)
    print("serving at port", PORT)
    logging.info('Starting httpd...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...')
