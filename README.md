# 🥋 Dojo – Student Management System

A comprehensive Django web application for students to manage their academic life.

## ✨ Features

- **📊 Dashboard** - Todo management with progress tracking
- **📅 Calendar** - Event scheduling with FullCalendar integration
- **📚 Courses** - Course organization with files and links
- **🕒 Schedule** - Weekly timetable view
- **⚙️ Settings** - User preferences and account management
- **👤 Profiles** - Student ID cards and personal information

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5.3.0 + Custom CSS
- **Database**: PostgreSQL
- **Calendar**: FullCalendar.js
- **Authentication**: Django Session-based

## 🚀 Quick Start

1. **Clone & Setup**
   ```bash
   git clone <repository>
   cd dojo
   pip install -r requirements.txt
   ```

2. **Database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Run**
   ```bash
   python manage.py runserver
   ```

4. **Visit**
   - http://127.0.0.1:8000/ (Welcome)
   - http://127.0.0.1:8000/dashboard/ (Dashboard)

## 📁 Structure

```
dojo/
├── apps/
│   ├── accounts/      # User auth & profiles
│   ├── dashboard/     # Todos & home
│   ├── courses/       # Course management
│   ├── calendarapp/   # Events & calendar
│   ├── schedule/      # Weekly timetable
│   └── settingsapp/   # User settings
├── templates/         # HTML templates
├── static/           # CSS, JS, images
└── media/            # User uploads
```

## 📖 Documentation

- **API Documentation**: [`API_DOCUMENTATION.md`](API_DOCUMENTATION.md)
- **Features**: Dashboard, Calendar, Courses, Schedule, Settings
- **Authentication**: Session-based with CSRF protection

## 🎯 Core Functionality

- **Todo Management**: Create, edit, delete, and track progress
- **Event Calendar**: Schedule classes, exams, and personal events
- **Course Organization**: Upload files, store links, manage assignments
- **Weekly Schedule**: Visual timetable with drag-and-drop
- **User Settings**: Customize week start, change password, delete account

## 🔒 Security

- Session-based authentication
- CSRF protection on all forms
- User-specific data isolation
- Input validation and sanitization

---

**Dojo** - Master your academic journey! 🎓