import json
import os
from datetime import datetime

DATABASE_FILE = 'students.json'

def load_database():
    """Load student data from JSON file"""
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_database(data):
    """Save student data to JSON file"""
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_student(username, password, name, email, roll_no, phone):
    """Add a new student to the database"""
    students = load_database()
    
    if username in students:
        return False, "Username already exists!"
    
    students[username] = {
        'password': password,
        'name': name,
        'email': email,
        'roll_no': roll_no,
        'phone': phone,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    save_database(students)
    return True, "Student registered successfully!"

def verify_login(username, password):
    """Verify student login credentials"""
    students = load_database()
    
    if username not in students:
        return False, "Username not found!"
    
    if students[username]['password'] != password:
        return False, "Incorrect password!"
    
    return True, students[username]

def get_student_info(username):
    """Get student information"""
    students = load_database()
    
    if username not in students:
        return None
    
    return students[username]

def update_student(username, **kwargs):
    """Update student information"""
    students = load_database()
    
    if username not in students:
        return False, "Student not found!"
    
    for key, value in kwargs.items():
        if key in students[username]:
            students[username][key] = value
    
    save_database(students)
    return True, "Student information updated successfully!"

def delete_student(username):
    """Delete a student from the database"""
    students = load_database()
    
    if username not in students:
        return False, "Student not found!"
    
    del students[username]
    save_database(students)
    return True, "Student deleted successfully!"

def get_all_students():
    """Get all students (Admin only)"""
    return load_database()
