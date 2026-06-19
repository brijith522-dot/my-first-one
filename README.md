# Student Management System

A complete student management system with user authentication, student profiles, and admin panel.

## Features

✅ **Student Features:**
- User Registration
- Secure Login with username and password
- View Profile
- Update Password
- Update Contact Information

✅ **Admin Features:**
- Admin Login (default: admin/admin123)
- Add New Students
- View All Students
- View Individual Student Details
- Delete Students

## Requirements

- Python 3.6 or higher
- No external dependencies (uses Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/brijith522-dot/my-first-one.git
cd my-first-one
```

2. Switch to the student-management-system branch:
```bash
git checkout student-management-system
```

## How to Run

1. Open terminal/command prompt
2. Navigate to the project directory
3. Run the main program:
```bash
python main.py
```

## Usage

### For Students:

1. **Register:** Choose option 2 from main menu and fill in your details
2. **Login:** Choose option 1 and enter your credentials
3. **Dashboard:** After login, you can:
   - View your profile
   - Update your password
   - Update your contact information

### For Admin:

1. Choose option 3 from main menu
2. Login with credentials:
   - Username: `admin`
   - Password: `admin123`
3. From admin dashboard, you can:
   - Add new students
   - View all students
   - View student details
   - Delete students

## File Structure

```
├── main.py              # Main entry point
├── database.py          # Database operations
├── student_portal.py    # Student features
├── admin_panel.py       # Admin features
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── students.json        # Student data (auto-created)
```

## Data Storage

All student data is stored in `students.json` file in JSON format.

## Example Usage

### Register as Student:
```
Username: john_doe
Password: password123
Name: John Doe
Email: john@example.com
Roll No: 001
Phone: 9876543210
```

### Default Admin Credentials:
```
Username: admin
Password: admin123
```

## Security Notes

- Passwords are stored in plain text (for educational purposes)
- For production use, implement proper password hashing
- Use environment variables for sensitive data
- Implement proper authentication protocols

## Future Enhancements

- [ ] Password hashing with bcrypt
- [ ] Database migration to SQL (SQLite/MySQL)
- [ ] Email verification
- [ ] OTP-based authentication
- [ ] Student grades and marks tracking
- [ ] Course enrollment system
- [ ] Web interface with Flask/Django

## License

Open source - Feel free to use and modify

## Author

Brijith - Learning Project
