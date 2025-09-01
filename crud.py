from http.server import HTTPServer,SimpleHTTPRequestHandler

class Crud_request_handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type",'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hello! This is your CRUD server.</h1>")

port = 7878
def run():
    live_server = HTTPServer(("localhost",port),Crud_request_handler)
    print(f"Server running at: http://localhost:{port}")
    live_server.serve_forever()
if __name__=="__main__":
    run()
