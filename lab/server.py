# Import Flask class from the flask module
from flask import Flask, jsonify, make_response, request

# Create an instance of the Flask class with the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    # Function that sends requests to the root URL
    # return "Hello, World!"
    # A dictionary like this returns a JSON instead of HTML
    return {"message": "Hello World"}

@app.route("/no_content")
def no_content():
    # Output returned as a tuple
    return {"message": "No content found"}, 204

@app.route("/exp")
def index_explicit():
    # Custom output using make_response() – import from flask
    out = make_response({"message": "Explicit index"})
    out.status_code = 200
    return out

@app.route("/data")
def get_data():
    try:
        # check if 'data' exists (in the URL) and has length greater than zero
        if data and len(data) > 0:
            # Return a JSON response indicating data found and its length
            return {"message": f"Data found of length {len(data)}"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500

    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

@app.route("/name_search")
def name_search():
    """Find a person in the database.
        Returns:
            json: Person if found, with status of 200
            404: If not found
            422: If argument 'q' is missing
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    if not query:
        # Return a JSON response with a message indicating 'q' is missing and a 422 Unprocessable Entity status code
        return {"message": "Query parameter 'q' is missing."}, 422

    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() == person["first_name"].lower():   # From our list of JSONs, person is a JSON
            return person, 200  # Note that person is already a JSON

    # If no match found
    return {"message": "Person not found"}, 404

@app.get("/count")  # equivalent to @app.get("/count", methods = ['GET'])
def count():
    try:
        return {"data count": len(data)}, 200
    except NameError:
        return {"message": "data not defined"}, 500

@app.get("/person/<uuid>")
def find_by_uuid(uuid):
    for person in data:
        if str(uuid) == person["id"]:
            return person

    # If not found
    return {"message": "Person not found"}, 404

@app.route("/person/<uuid>", methods = ['DELETE'])
def delete_by_uuid(uuid):
    for person in data:
        if str(uuid) == person["id"]:
            data.remove(person)
            return {"message": "Person removed successfully"}, 200

    # If not found
    return {"message": "Person not found"}, 404

@app.route("/person", methods = ['POST'])
def add_by_uuid():
    try:
        new_person = request.get_json()

        if new_person is None or "id" not in new_person:
            return {"message": "Bad request."}, 400

        for person in data:
            if new_person["id"] == person["id"]:
                return {"message": "A person already exists with this ID."}, 409

        data.append(new_person)
        return {"message": f"Person with ID {new_person['id']} created successfully."}, 201

    except NameError:
        return {"Server error": "Data is not initialised."}, 500

@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"error": "API not found."}, 404

# Some hard-coded sample data below

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Jahnavi",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Anushka",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]