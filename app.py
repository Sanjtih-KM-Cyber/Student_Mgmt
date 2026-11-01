from flask import Flask, jsonify, request
app = Flask(__name__)
students = {}
next_id = 1
@app.route("/")
def home():
    return "Student Management System is Running!"
@app.route("/about")
def about():
    return jsonify(
        project="Student Management System",
        version="1.0"
    )
@app.route("/health")
def health():
    return jsonify(status="ok")
@app.route("/students", methods=["POST"])
def add_student():
    global next_id
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify(error="Name is required"), 400
    student = {
        "id": next_id,
        "name": name
    }
    students[next_id] = student
    next_id += 1
    return jsonify(student), 201
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(list(students.values()))
if __name__ == "__main__":
    app.run(debug=True)