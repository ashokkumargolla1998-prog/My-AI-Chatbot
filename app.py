from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>DevOps Training App</title>
        </head>
        <body>
            <h1>Welcome to My DevOps Application!</h1>
            <p>My Python web server is running successfully.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))


def create_server(host="0.0.0.0", port=8000):
    return HTTPServer((host, port), MyHandler)


if __name__ == "__main__":
    server = create_server()
    print("DevOps application running on port 8000")
    server.serve_forever()