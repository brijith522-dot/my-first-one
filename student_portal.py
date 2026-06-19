from database import verify_login, get_student_info, update_student
import getpass

def student_dashboard(username):
    """Display student dashboard"""
    while True:
        print("\n" + "="*50)
        print("       STUDENT DASHBOARD")
        print("="*50)
        print("1. View My Profile")
        print("2. Update My Password")
        print("3. Update My Contact Info")
        print("4. Logout")
        print("="*50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            view_profile(username)
        elif choice == '2':
            update_password(username)
        elif choice == '3':
            update_contact_info(username)
        elif choice == '4':
            print("\nLogging out...")
            break
        else:
            print("\n❌ Invalid choice! Please try again.")

def view_profile(username):
    """View student profile"""
    student = get_student_info(username)
    
    if student:
        print("\n" + "="*50)
        print("       MY PROFILE")
        print("="*50)
        print(f"Username:  {username}")
        print(f"Name:      {student['name']}")
        print(f"Email:     {student['email']}")
        print(f"Roll No:   {student['roll_no']}")
        print(f"Phone:     {student['phone']}")
        print(f"Joined:    {student['created_at']}")
        print("="*50)
    else:
        print("\n❌ Error retrieving profile!")

def update_password(username):
    """Update student password"""
    print("\n" + "="*50)
    print("       UPDATE PASSWORD")
    print("="*50)
    
    old_password = getpass.getpass("Enter current password: ")
    
    # Verify old password
    success, _ = verify_login(username, old_password)
    if not success:
        print("\n❌ Current password is incorrect!")
        return
    
    new_password = getpass.getpass("Enter new password: ")
    confirm_password = getpass.getpass("Confirm new password: ")
    
    if new_password != confirm_password:
        print("\n❌ Passwords do not match!")
        return
    
    if len(new_password) < 4:
        print("\n❌ Password must be at least 4 characters!")
        return
    
    success, msg = update_student(username, password=new_password)
    if success:
        print(f"\n✅ {msg}")
    else:
        print(f"\n❌ {msg}")

def update_contact_info(username):
    """Update student contact information"""
    print("\n" + "="*50)
    print("       UPDATE CONTACT INFO")
    print("="*50)
    
    print("\nLeave blank to keep current information.")
    
    new_email = input("Enter new email (or press Enter to skip): ").strip()
    new_phone = input("Enter new phone (or press Enter to skip): ").strip()
    
    updates = {}
    if new_email:
        updates['email'] = new_email
    if new_phone:
        updates['phone'] = new_phone
    
    if updates:
        success, msg = update_student(username, **updates)
        if success:
            print(f"\n✅ {msg}")
        else:
            print(f"\n❌ {msg}")
    else:
        print("\nℹ️ No changes made.")
