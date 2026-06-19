from student_portal import student_dashboard
from admin_panel import admin_login, admin_dashboard
from database import verify_login, add_student
import getpass

def main_menu():
    """Display main menu"""
    while True:
        print("\n" + "="*50)
        print("   STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Student Login")
        print("2. Student Registration")
        print("3. Admin Login")
        print("4. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            student_login()
        elif choice == '2':
            student_registration()
        elif choice == '3':
            if admin_login():
                admin_dashboard()
        elif choice == '4':
            print("\n👋 Thank you for using Student Management System!")
            print("Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")

def student_login():
    """Handle student login"""
    print("\n" + "="*50)
    print("       STUDENT LOGIN")
    print("="*50)
    
    username = input("\nUsername: ").strip()
    password = getpass.getpass("Password: ")
    
    success, result = verify_login(username, password)
    
    if success:
        print(f"\n✅ Login successful! Welcome {result['name']}!")
        student_dashboard(username)
    else:
        print(f"\n❌ {result}")

def student_registration():
    """Handle student registration"""
    print("\n" + "="*50)
    print("       STUDENT REGISTRATION")
    print("="*50)
    
    username = input("\nCreate username: ").strip()
    password = getpass.getpass("Create password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    
    if password != confirm_password:
        print("\n❌ Passwords do not match!")
        return
    
    if len(password) < 4:
        print("\n❌ Password must be at least 4 characters!")
        return
    
    name = input("Full Name: ").strip()
    email = input("Email: ").strip()
    roll_no = input("Roll No: ").strip()
    phone = input("Phone: ").strip()
    
    if not all([username, password, name, email, roll_no, phone]):
        print("\n❌ All fields are required!")
        return
    
    success, msg = add_student(username, password, name, email, roll_no, phone)
    if success:
        print(f"\n✅ {msg} You can now login!")
    else:
        print(f"\n❌ {msg}")

if __name__ == "__main__":
    main_menu()
