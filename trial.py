from http.server import HTTPServer,SimpleHTTPRequestHandler

port = 8000
class BookingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path =='/'or self.path == "/index.html":
            self.serve_template("index.html")
    def serve_template(self,file_path):
        with open(f"templates/{file_path}",'rb') as file:
            content = file.read()
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(content)
            
def run():
    live_server = HTTPServer(("localhost",port),BookingHandler)
    print(f"Server running at: http://localhost:{port}")
    live_server.serve_forever()
if __name__ =='__main__':
    run()