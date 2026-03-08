# REST APIs in flask framework
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (like a database)
students = {
    1: {"name": "Abhishek", "age": 21},
    2: {"name": "Rahul", "age": 22}
}

# GET → fetch all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST → add a new student
@app.route("/students", methods=["POST"])
def add_student():

    data = request.json
    new_id = len(students) + 1

    students[new_id] = data

    return jsonify({"message": "Student added", "data": students[new_id]})


# PUT → update student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    if id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.json
    students[id] = data

    return jsonify({"message": "Student updated", "data": students[id]})


# DELETE → remove student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    if id not in students:
        return jsonify({"error": "Student not found"}), 404

    deleted = students.pop(id)

    return jsonify({"message": "Student deleted", "data": deleted})


if __name__ == "__main__":
    app.run(debug=True)