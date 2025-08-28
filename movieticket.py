from http.server import HTTPServer,SimpleHTTPRequestHandler

class Moviehall:
    def __init__(self,total_seats):
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats<self.total_seats:
            self.booked_seats+=1
            return True
        return False
    
    def remaining_seats(self):
        return self.total_seats-self.booked_seats

hall = Moviehall(50)

#http requesthandler
class BookingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/' or self.path=='index.html':
            
            html = f"""
            <html>
            <head><title>Movie Hall Ticket Booking</title></head>
            <body>
                <h1>Movie Hall Seat Booking</h1>
                <p>Total seats: {hall.total_seats}</p>
                <p>Booked seats: {hall.booked_seats}</p>
                <p>Remaining seats: {hall.remaining_seats()}</p>

                <form method="POST">
                    <button type="submit">Book a Seat</button>
                </form>
            </body>
            </html>
            """

            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found")
            

    def do_POST(self):
        if hall.book_seat():
            message = "seat booked sucessfully"
        else:
            message = "All seats are already booked"

        html = f"""
        <html>
        <head><title>Booking Result</title></head>
        <body>
            <h1>{message}</h1>
            <p>Total seats: {hall.total_seats}</p>
            <p>Booked seats: {hall.booked_seats}</p>
            <p>Remaining seats: {hall.remaining_seats()}</p>

            <a href="/">Go back</a>
        </body>
        </html>
        """

        # ✅ send headers before writing HTML
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))


    # def serve_template(self,file_path):
    #     with open(f"templates/{file_path}",'rb') as file:
    #         content = file.read()

    #     self.send_response(200)
    #     self.send_header("Content-type",'text/html')
    #     self.end_headers()
    #     self.wfile.write(content)

# run the server
port = 8000
def run():
    server = HTTPServer(('localhost', port), BookingHandler)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()


print(__name__)

if __name__=="__main__":
    run()
