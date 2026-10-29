from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
          <body>
            <h1>My First DevOps Web Server!</h1>
            <p>My local server is working.</p>
          </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(("127.0.0.1", 8000), MyHandler)
print("Server running at http://127.0.0.1:8000")
server.serve_forever()
