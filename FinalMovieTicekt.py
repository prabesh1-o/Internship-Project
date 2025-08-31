from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class TicketHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse URL and query parameters
        parsed = urlparse(self.path)
        path = parsed.path
        query = {k: v[0] for k, v in parse_qs(parsed.query).items()}

        # Map paths to views
        routes = {
            "/": views_home,
            "/create": views_create,
            "/update": views_update,
            "/delete": views_delete
        }

        view_func = routes.get(path)
        if view_func:
            response = view_func(query)
        else:
            response = "404 Not Found"

        # Send response
        self.send_response(200)
        # Home page uses HTML, others plain text
        self.send_header("Content-type", "text/html" if path == "/" else "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.booked = False

    def book(self):
        if not self.booked:
            self.booked = True
            return True
        return False

    def __str__(self):
        return "Booked" if self.booked else f"{self.row}-{self.col}"

class MovieHall:
    def __init__(self, name, rows, cols):
        self.name = name
        self.rows = rows
        self.cols = cols
        self.seats = [[Seat(i+1, j+1) for j in range(cols)] for i in range(rows)]

    def book_seat(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.seats[row][col].book()
        return False

    def seat_summary(self):
        total = self.rows * self.cols
        booked = sum(seat.booked for row in self.seats for seat in row)
        remaining = total - booked
        return total, booked, remaining

halls = {
    "Vip": MovieHall("Vip", 5, 5),
    "Regular": MovieHall("Regular", 3, 5)
}

# --- Views ---
def views_home(query=None):
    html = "<h1>Movie Hall Booking</h1>"

    # Show all halls and their seat layout
    if not halls:
        html += "<p>No halls available</p>"
    else:
        for name, hall in halls.items():
            total, booked, remaining = hall.seat_summary()
            html += f"<h3>{name} - Total: {total}, Booked: {booked}, Remaining: {remaining}</h3>"
            html += "<table border='1' cellspacing='5'>"
            for r in hall.seats:
                html += "<tr>"
                for seat in r:
                    color = "red" if seat.booked else "green"
                    html += f"<td><a href='/update?name={name}&row={seat.row}&col={seat.col}' style='display:block;width:40px;height:40px;background:{color};text-align:center;text-decoration:none;color:white;'>{seat.row}-{seat.col}</a></td>"
                html += "</tr>"
            html += "</table><br>"

    # Create hall form
    html += """
    <h3>Create Hall</h3>
    <form action="/create" method="get">
      Name: <input name="name">
      Rows: <input name="rows" type="number">
      Cols: <input name="cols" type="number">
      <input type="submit" value="Create">
    </form>
    """

    # Delete hall form
    html += """
    <h3>Delete Hall</h3>
    <form action="/delete" method="get">
      Name: <input name="name">
      <input type="submit" value="Delete">
    </form>
    """

    return html
 
# Create hall
def views_create(query):
    name = query.get("name")
    rows = int(query.get("rows", 0))
    cols = int(query.get("cols", 0))
    if not name or rows <= 0 or cols <= 0:
        return "Invalid parameter"

    if name in halls:
        return f"Hall '{name}' already exists"

    halls[name] = MovieHall(name, rows, cols)
    return f"Hall '{name}' created. <a href='/'>Go Back</a>"

# Book seat
def views_update(query):
    name = query.get("name")
    row = int(query.get("row", -1)) - 1
    col = int(query.get("col", -1)) - 1
    hall = halls.get(name)

    if not hall:
        return f"Hall '{name}' not found. <a href='/'>Go Back</a>"

    if hall.book_seat(row, col):
        return f"Seat {row+1}-{col+1} booked in '{name}'. <a href='/'>Go Back</a>"
    return f"Seat {row+1}-{col+1} already booked or invalid. <a href='/'>Go Back</a>"

# Delete hall
def views_delete(query):
    name = query.get("name")
    if name in halls:
        halls.pop(name)
        return f"Hall '{name}' deleted. <a href='/'>Go Back</a>"
    return f"Hall '{name}' not found. <a href='/'>Go Back</a>"

# Run server
port = 7878
def run():
    server = HTTPServer(("localhost", port), TicketHandler)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()

if __name__ == "__main__":
    run()
