from database import add_student, get_all_students, delete_student, get_student_info
import getpass

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_login():
    """Authenticate admin"""
    print("\n" + "="*50)
    print("       ADMIN LOGIN")
    print("="*50)
    
    username = input("\nUsername: ").strip()
    password = getpass.getpass("Password: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    else:
        print("\n❌ Invalid admin credentials!")
        return False

def admin_dashboard():
    """Display admin dashboard"""
    while True:
        print("\n" + "="*50)
        print("       ADMIN DASHBOARD")
        print("="*50)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. View Student Details")
        print("4. Delete Student")
        print("5. Logout")
        print("="*50)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            add_new_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            view_student_details()
        elif choice == '4':
            delete_student_admin()
        elif choice == '5':
            print("\nLogging out from admin panel...")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")

def add_new_student():
    """Add a new student"""
    print("\n" + "="*50)
    print("       ADD NEW STUDENT")
    print("="*50)
    
    username = input("\nUsername: ").strip()
    password = getpass.getpass("Password: ")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    roll_no = input("Roll No: ").strip()
    phone = input("Phone: ").strip()
    
    if not all([username, password, name, email, roll_no, phone]):
        print("\n❌ All fields are required!")
        return
    
    if len(password) < 4:
        print("\n❌ Password must be at least 4 characters!")
        return
    
    success, msg = add_student(username, password, name, email, roll_no, phone)
    if success:
        print(f"\n✅ {msg}")
    else:
        print(f"\n❌ {msg}")

def view_all_students():
    """View all students"""
    print("\n" + "="*50)
    print("       ALL STUDENTS")
    print("="*50)
    
    students = get_all_students()
    
    if not students:
        print("\n❌ No students found!")
        return
    
    print(f"\n{'Username':<15} {'Name':<20} {'Roll No':<10} {'Email':<25}")
    print("-" * 70)
    
    for username, data in students.items():
        print(f"{username:<15} {data['name']:<20} {data['roll_no']:<10} {data['email']:<25}")
    
    print(f"\nTotal Students: {len(students)}")
    print("="*50)

def view_student_details():
    """View detailed information of a student"""
    print("\n" + "="*50)
    print("       VIEW STUDENT DETAILS")
    print("="*50)
    
    username = input("\nEnter student username: ").strip()
    student = get_student_info(username)
    
    if student:
        print("\n" + "="*50)
        print(f"Student: {username}")
        print("="*50)
        print(f"Name:     {student['name']}")
        print(f"Email:    {student['email']}")
        print(f"Roll No:  {student['roll_no']}")
        print(f"Phone:    {student['phone']}")
        print(f"Joined:   {student['created_at']}")
        print("="*50)
    else:
        print("\n❌ Student not found!")

def delete_student_admin():
    """Delete a student"""
    print("\n" + "="*50)
    print("       DELETE STUDENT")
    print("="*50)
    
    username = input("\nEnter student username to delete: ").strip()
    
    confirm = input(f"Are you sure you want to delete {username}? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        success, msg = delete_student(username)
        if success:
            print(f"\n✅ {msg}")
        else:
            print(f"\n❌ {msg}")
    else:
        print("\nℹ️ Deletion cancelled.")
