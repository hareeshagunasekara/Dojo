# 🥋 Dojo – Your Student Space, Simplified

Just like a dojo is a place where people come together to train, grow, and master their skills, **Dojo** is your digital hub for learning and organizing your student life.

## ✨ Features

- **🎯 Stay on track** with to-dos that actually get done
- **📚 Organize courses** with files, links, and reminders all in one spot
- **📅 Plan smarter** with a personal calendar and event manager
- **🕒 Never miss class** with a clean weekly timetable view
- **⚙️ Make it yours** with customizable settings and a unique Student ID

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: Django Templates + Bootstrap 5.3.0 (CDN)
- **Database**: PostgreSQL 14.19
- **Styling**: Bootstrap + Custom CSS
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Static Files**: WhiteNoise

## 📁 Project Structure

```
dojo/
├── manage.py
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── Dockerfile             # Docker configuration
├── compose/               # Docker Compose & Nginx
│   ├── docker-compose.yml
│   └── nginx.conf
├── dojo/                  # Django project package
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── settings/          # Split settings for dev/prod
│       ├── __init__.py    # Imports base + local overrides
│       ├── base.py        # Common settings
│       ├── dev.py         # Development settings
│       └── prod.py        # Production settings
├── apps/                  # Django applications
│   ├── accounts/          # User authentication & profiles
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── models.py      # StudentProfile model
│   │   ├── views.py       # Signup, login, profile views
│   │   ├── urls.py        # Account URLs
│   │   ├── forms.py       # User forms
│   │   ├── signals.py     # Auto-create student profiles
│   │   ├── services.py    # Business logic
│   │   ├── selectors.py   # Data retrieval
│   │   └── tests/         # Test files
│   ├── dashboard/         # Home dashboard & personal todos
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py      # Todo model
│   │   ├── views.py       # Dashboard views
│   │   ├── urls.py        # Dashboard URLs
│   │   ├── forms.py       # Todo forms
│   │   └── tests/         # Test files
│   ├── courses/           # Course management
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py      # Course, CourseFile, CourseLink, CourseTodo
│   │   ├── views.py       # Course views
│   │   ├── urls.py        # Course URLs
│   │   ├── forms.py       # Course forms
│   │   └── tests/         # Test files
│   ├── calendarapp/       # Calendar & events
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py      # Event model
│   │   ├── views.py       # Calendar views
│   │   ├── urls.py        # Calendar URLs
│   │   ├── forms.py       # Event forms
│   │   └── tests/         # Test files
│   ├── schedule/          # Weekly timetable
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py      # ClassSchedule model
│   │   ├── views.py       # Schedule views
│   │   ├── urls.py        # Schedule URLs
│   │   ├── forms.py       # Schedule forms
│   │   └── tests/         # Test files
│   └── settingsapp/       # User settings & preferences
│       ├── __init__.py
│       ├── apps.py
│       ├── views.py       # Settings views
│       ├── urls.py        # Settings URLs
│       ├── forms.py       # Settings forms
│       └── tests/         # Test files
├── templates/             # HTML templates
│   ├── base.html          # Base template with Bootstrap
│   ├── components/        # Reusable components
│   │   ├── navbar.html    # Navigation bar
│   │   ├── sidebar.html   # Sidebar navigation
│   │   ├── messages.html  # Flash messages
│   │   └── footer.html    # Footer
│   ├── accounts/          # Account templates
│   ├── dashboard/         # Dashboard templates
│   ├── courses/           # Course templates
│   ├── calendarapp/       # Calendar templates
│   ├── schedule/          # Schedule templates
│   └── settingsapp/       # Settings templates
├── static/               # Static files
│   ├── dojo.css          # Custom styles
│   ├── dojo.js           # Custom JavaScript
│   └── img/              # Images
├── media/                # User uploads
│   ├── avatars/          # User profile pictures
│   └── course_files/     # Course-related files
├── logs/                 # Application logs
└── tests/                # Cross-app integration tests
    └── __init__.py
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 14+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Dojo
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL**
   ```bash
   # Create database and user (if not already done)
   createdb mydb
   createuser myuser --interactive --pwprompt
   # Enter password: hareesha123
   # Make superuser: y
   ```

5. **Configure environment variables**
   ```bash
   # Edit .env file with your settings
   DEBUG=True
   SECRET_KEY=your-secret-key-here-change-in-production
   DATABASE_URL=postgresql://myuser:hareesha123@localhost:5432/mydb
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Set up settings (optional)**
   ```bash
   # For development (default)
   export DJANGO_SETTINGS_MODULE=dojo.settings.dev
   
   # For production
   export DJANGO_SETTINGS_MODULE=dojo.settings.prod
   ```

8. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

9. **Run the development server**
   ```bash
   # Option 1: Using the runner script (recommended)
   python run_dev.py
   
   # Option 2: Using Django directly
   python manage.py runserver
   
   # Option 3: Set environment variable explicitly
   export DJANGO_SETTINGS_MODULE=dojo.settings.dev
   python manage.py runserver
   ```

10. **Visit the application**
    - Open http://127.0.0.1:8000/ in your browser
    - Admin interface: http://127.0.0.1:8000/admin/

## 🎯 Core Features

### Dashboard
- **Personal Todo Management**: Create, edit, delete, and mark todos as complete
- **Progress Tracking**: Visual statistics showing completed vs pending tasks
- **Priority Levels**: Organize todos by low, medium, or high priority
- **Due Dates**: Set deadlines for important tasks

### Course Management
- **Course Organization**: Add courses with codes, descriptions, and instructors
- **File Management**: Upload and organize course-related files
- **Link Collection**: Store important course links and resources
- **Course-specific Todos**: Create todos specific to each course

### Calendar & Events
- **Event Management**: Schedule classes, exams, assignments, and personal events
- **Event Types**: Categorize events (class, exam, assignment, meeting, personal)
- **Date & Time**: Set start and end times for events
- **Location Tracking**: Add location information for events

### Weekly Schedule
- **Timetable View**: Clean weekly schedule showing all classes
- **Class Details**: Room numbers, instructors, and time slots
- **Day Organization**: Classes organized by day of the week

### User Profiles
- **Student ID**: Unique identifier automatically generated for each user
- **Profile Customization**: Bio, avatar, phone number, and date of birth
- **Settings Management**: Theme preferences, language, timezone, and notifications

## 🔧 Configuration

### Database Configuration
The application is configured to use PostgreSQL by default. Update the database settings in `studenthub/settings.py` if needed.

### Static Files
Static files are served using WhiteNoise in development. For production, configure your web server to serve static files.

### Environment Variables
Create a `.env` file in the project root with the following variables:
- `DEBUG`: Set to `True` for development, `False` for production
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## 🎨 Customization

### Styling
- Custom CSS is in `static/css/app.css`
- Bootstrap 5.3.0 is loaded via CDN
- Bootstrap Icons are included for consistent iconography

### JavaScript
- Custom JavaScript is in `static/js/app.js`
- Includes interactive features like todo toggling, form validation, and dynamic content loading

### Templates
- All templates extend `base.html`
- Components are modular and reusable
- Bootstrap classes are used for responsive design

## 🔒 Security Features

- **User Authentication**: Django's built-in authentication system
- **CSRF Protection**: Enabled by default
- **Form Validation**: Server-side validation for all forms
- **File Upload Security**: Restricted file types and sizes
- **SQL Injection Protection**: Django ORM prevents SQL injection

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

Bootstrap 5 provides responsive grid system and components.

## 🚀 Deployment

### Traditional Deployment

For production deployment:

1. Set `DEBUG=False` in settings
2. Configure a production database
3. Set up a proper web server (nginx + gunicorn recommended)
4. Configure static file serving
5. Set up SSL/HTTPS
6. Use environment variables for sensitive settings

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   cd compose
   docker-compose up --build
   ```

### Production Deployment

1. **Run with production settings**
   ```bash
   # Option 1: Using the runner script
   python run_prod.py
   
   # Option 2: Using Django directly
   export DJANGO_SETTINGS_MODULE=dojo.settings.prod
   python manage.py runserver
   ```

2. **Run migrations in Docker**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Create superuser in Docker**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Collect static files**
   ```bash
   docker-compose exec web python manage.py collectstatic --noinput
   ```

The application will be available at:
- Web: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Nginx: http://localhost:80/ (if using nginx service)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the Django documentation
- Review the code comments

---

**Dojo** - Master your academic journey! 🎓