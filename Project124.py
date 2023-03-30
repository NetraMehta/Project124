from flask import Flask, jsonify, request

app = Flask(__name__)

Contacts = [
    {
        "id": 1,
        "Name": "John",
        "Contact": 9876543210,
        "done": False
    },
    {
        "id": 2,
        "Name": "Alex",
        "Contact": 1234567890,
        "done": False
    }
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please enter the data!"
        }, 400)
    
    Contact = {
        "id": Contacts[-1]["id"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "done": False
    }

    Contacts.append(Contact)
    return jsonify({
        "status": "success",
        "message": "Contact added succesfully!"
    })

if (__name__ == "__main__"):
    app.run(debug = True)