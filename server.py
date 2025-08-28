from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib

port = 8080


class BookingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.serve_template("index.html")
            # self.wfile.write(b"<h1>Hello</h1>")

    def serve_template(self, file_path):
        with open(f"templates/{file_path}", "rb") as file:
            content = file.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content)


class Seat:
    def __init__(self, row, col):
        self.rows = row
        self.cols = col
        self.booked = False

    def book(self):
        if not self.booked:
            self.booked = True
            return True
        return False

    def __str__(self):
        return "Booked" if self.booked else f"{self.rows}-{self.cols}"


class MovieHall:
    def __init__(self, rows, cols):
        self.seats = []
        for i in range(rows):
            row_seat = []
            for j in range(cols):
                seat = Seat(i + 1, j + 1)
                row_seat.append(seat)

            self.seats.append(row_seat)

    def book_seat(self, row, col):
        if 0 <= row < (len(self.seats)) and 0 <= col < len(self.seats[0]):
            return self.seats[row][col].book()
        return False

    def seat_summary(self):
        total = len(self.seats) * len(self.seats[0])
        booked = 0
        for row in self.seats:
            for seats in row:
                if seats.booked:
                    booked += 1
        remaining = total - booked
        return total, booked, remaining


hall = MovieHall(5, 5)


def run():
    live_server = HTTPServer(("localhost", port), BookingHandler)
    print(f"Server running at: http://localhost:{port}")
    live_server.serve_forever()


if __name__ == "__main__":
    run()
