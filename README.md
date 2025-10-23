# Personal Portfolio Website

A Flask-based personal portfolio website showcasing projects, resume, and contact information.

## Features

- **Template-based Architecture**: Uses Jinja2 templates for clean separation of concerns
- **Database-backed Projects**: SQLite database stores project information dynamically
- **Responsive Design**: Modern, mobile-friendly CSS styling
- **Project Management**: Add, view, and manage projects through web interface

## Project Structure

```
AiDD_As5/
├── app.py                 # Main Flask application
├── DAL.py                 # Data Access Layer for SQLite operations
├── test_db.py            # Database testing script
├── projects.db           # SQLite database (created automatically)
├── templates/            # Jinja2 templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── resume.html       # Resume page
│   ├── projects.html     # Projects listing page
│   ├── add_project.html  # Add new project form
│   ├── contact.html      # Contact page
│   └── thankyou.html     # Thank you page
└── static/               # Static assets
    ├── css/
    │   └── styles.css    # Main stylesheet
    └── images/           # Image assets
        └── ProfilePic.JPG
```

## Database Schema

The `projects` table contains:
- `id`: Primary key (auto-increment)
- `title`: Project title
- `description`: Project description
- `image_filename`: Name of image file in static/images/
- `created_at`: Timestamp of creation

## Running the Application

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser to `http://localhost:5000`

## Database Operations

The application includes a Data Access Layer (DAL) with the following operations:
- `get_all_projects()`: Retrieve all projects (newest first)
- `get_project_by_id(id)`: Get specific project
- `add_project(title, description, image_filename)`: Add new project
- `update_project(id, title, description, image_filename)`: Update project
- `delete_project(id)`: Delete project

## Testing

Run the database test script:
```bash
python test_db.py
```

## Routes

- `/` - Home page
- `/about` - About page
- `/resume` - Resume page
- `/projects` - Projects listing (GET)
- `/projects/new` - Add project form (GET)
- `/projects` - Create project (POST)
- `/contact` - Contact page
- `/thankyou` - Thank you page

## Features Implemented

✅ Jinja2 template system
✅ SQLite database integration
✅ Dynamic projects page
✅ Add project form
✅ Responsive design maintained
✅ Static asset organization
✅ Database seeding for testing
✅ Error handling and validation
