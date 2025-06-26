# Trainer Management System

A simple Flask web application for managing trainer records using SQLite database.

## Features

- ✅ **Add New Trainers** - Form to input trainer details (First Name, Last Name, Designation, Course)
- ✅ **View All Trainers** - Display all trainer records in a formatted table
- ✅ **SQLite Database** - No external database server required
- ✅ **Responsive Design** - Clean and modern user interface
- ✅ **Navigation** - Easy movement between different pages

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite3 (built-in)
- **Frontend**: HTML5, CSS3
- **Template Engine**: Jinja2 (Flask's default)

## Project Structure

```
FLASK-App-with-MySQL-Database/
│
├── app.py                  # Main Flask application
├── alnafi.db              # SQLite database (auto-generated)
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
│
└── templates/             # HTML templates
    ├── home.html          # Landing page
    ├── trainer_details.html # Add trainer form
    ├── view_trainers.html # Display all trainers
    └── success.html       # Success confirmation page
```

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Flask

### Installation Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd FLASK-App-with-MySQL-Database
   ```

2. **Install Flask** (if not already installed)
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - Or access from other devices on the same network: `http://your-ip-address:5000`

## Usage

### Adding a New Trainer
1. Go to the home page
2. Click "Add New Trainer"
3. Fill in the required fields:
   - First Name
   - Last Name
   - Designation
   - Course
4. Click "Submit"

### Viewing All Trainers
1. From any page, click "View All Trainers"
2. Browse through the table of all trainer records
3. Records are displayed with ID, names, designation, course, and date added

## Database Schema

The application uses a single table `trainer_details` with the following structure:

| Column   | Type    | Description                    |
|----------|---------|--------------------------------|
| id       | INTEGER | Primary key (auto-increment)  |
| fname    | TEXT    | First name (required)          |
| lname    | TEXT    | Last name (required)           |
| design   | TEXT    | Designation (required)         |
| course   | TEXT    | Course (required)              |
| datetime | DATE    | Date record was added          |

## API Endpoints

| Route            | Method | Description                    |
|------------------|--------|--------------------------------|
| `/`              | GET    | Home page                      |
| `/trainer`       | GET    | Add trainer form               |
| `/trainer_create`| POST   | Process trainer form submission|
| `/view_trainers` | GET    | Display all trainers           |

## Configuration

### Database Configuration
- **Database Type**: SQLite3
- **Database File**: `alnafi.db` (auto-created in project root)
- **Auto-initialization**: Database and table are created automatically on first run

### Flask Configuration
- **Debug Mode**: Enabled (for development)
- **Host**: `0.0.0.0` (accessible from all network interfaces)
- **Port**: `5000` (default Flask port)

## Development

### Project History
This application was originally designed to work with MySQL but has been converted to use SQLite for easier setup and deployment without requiring a separate database server.

### Key Changes Made
- Replaced `flask_mysqldb` with built-in `sqlite3`
- Updated SQL syntax from MySQL to SQLite format
- Added automatic database initialization
- Improved user interface with modern styling
- Added comprehensive navigation between pages

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change the port in app.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Database file not found**
   - The database file `alnafi.db` is created automatically
   - Ensure the application has write permissions in the project directory

3. **Template not found errors**
   - Ensure all HTML files are in the `templates/` folder
   - Check file names match exactly (case-sensitive)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues or questions, please create an issue in the repository or contact the development team.

---

**Note**: This application is configured for development use. For production deployment, additional security measures and configuration changes are recommended.
