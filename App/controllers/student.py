from flask import jsonify
from App.models import Student
from App.database import db

# Creates a new student and adds them to the database
def create_student(name, degree):
    new_student = Student(name=name, degree=degree)
    db.session.add(new_student)
    db.session.commit()
    return new_student

# Gets all students in the database
def get_all_students():
    return Student.query.all()

# Gets all students in the database as a JSON object
def get_all_students_json():
    students = Students.query.all()
    if not students:
        return[]
    students = [students.to_json() for student in students]
    return students

# Gets a student by name
def get_students_by_name(name):
    return Student.query.filter_by(name=name).all()

# Gets all reviews for a given student as a JSON object
def get_all_student_reviews(name):
    student = Student.query.get(name)
    if not student:
        return {"error:" "this student does not exist"}, 404
    return [review.to_json for review in student.reviews], 200

