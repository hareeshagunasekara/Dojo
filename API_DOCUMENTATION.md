# 🥋 Dojo API Documentation

Quick reference for all API endpoints in the Dojo student management system.

## 🔐 Authentication

All endpoints require Django session authentication with CSRF tokens for POST/PUT/DELETE requests.

```javascript
headers: {
    'X-CSRFToken': getCookie('csrftoken'),
    'Content-Type': 'application/json',
}
```

## 📊 Dashboard API

### Get Dashboard Data
**GET** `/dashboard/`
```json
{
    "todos": [...],
    "statistics": {
        "completed_todos": 5,
        "ongoing_todos": 3,
        "missed_todos": 1,
        "total_todos": 9,
        "progress_percentage": 55
    }
}
```

### Toggle Todo
**POST** `/dashboard/todo/{todo_id}/toggle/`
```json
{"completed": true}
```

### Delete Todo
**POST** `/dashboard/todo/{todo_id}/delete/`

## 📅 Calendar API

### Get Events
**GET** `/calendar/`
```json
{
    "events": [
        {
            "id": 1,
            "title": "Math Exam",
            "start_date": "2024-01-15",
            "start_time": "14:00:00",
            "event_type": "exam"
        }
    ]
}
```

### Create Event (AJAX)
**POST** `/calendar/event/add/ajax/`
```json
{
    "title": "Team Meeting",
    "start_date": "2024-01-15",
    "start_time": "10:00",
    "end_date": "2024-01-15",
    "end_time": "11:00",
    "event_type": "meeting"
}
```

### Update Event
**POST** `/calendar/event/{event_id}/update/`
```json
{
    "start_date": "2024-01-16",
    "start_time": "14:00:00"
}
```

### Delete Event
**POST** `/calendar/event/{event_id}/delete/ajax/`

## 📚 Courses API

### Get Courses
**GET** `/courses/`
```json
{
    "courses": [
        {
            "id": 1,
            "name": "Web Development",
            "code": "CS101",
            "instructor": "Dr. Smith"
        }
    ]
}
```

### Get Courses for Calendar
**GET** `/courses/api/courses/`
```json
[
    {"id": 1, "name": "Web Development"},
    {"id": 2, "name": "Calculus"}
]
```

### Create Course
**POST** `/courses/add/`
```json
{
    "name": "Data Structures",
    "code": "CS201",
    "description": "Advanced algorithms",
    "instructor": "Dr. Johnson"
}
```

### Update Course
**POST** `/courses/{course_id}/edit/`

### Delete Course
**POST** `/courses/{course_id}/delete/`

### Upload Course Image
**POST** `/courses/{course_id}/upload-image/`
```
Content-Type: multipart/form-data
image: [file]
```

### Get Course Files
**GET** `/courses/{course_id}/files/`

### Add Course File
**POST** `/courses/{course_id}/files/add/`
```
Content-Type: multipart/form-data
name: "Assignment 1"
file: [file]
```

### Get Course Links
**GET** `/courses/{course_id}/links/`

### Add Course Link
**POST** `/courses/{course_id}/links/add/`
```json
{
    "title": "GitHub Repository",
    "url": "https://github.com/example/repo"
}
```

## 🕒 Schedule API

### Get Schedule
**GET** `/schedule/`
```json
{
    "schedules": [
        {
            "id": 1,
            "title": "Web Development",
            "instructor": "Dr. Smith",
            "room_location": "Room 101",
            "slots": [...]
        }
    ]
}
```

### Create Schedule
**POST** `/schedule/add/`
```json
{
    "title": "Calculus",
    "instructor": "Dr. Johnson",
    "room_location": "Room 202",
    "color": "#BFECFF"
}
```

### Update Schedule
**POST** `/schedule/{schedule_id}/edit/`

### Delete Schedule
**POST** `/schedule/{schedule_id}/delete/`

### Add Schedule Slot
**POST** `/schedule/{schedule_id}/add-slot/`
```json
{
    "day_of_week": "wednesday",
    "start_time": "16:00",
    "end_time": "17:30"
}
```

## ⚙️ Settings API

### Get Settings
**GET** `/settings/`
```json
{
    "user_settings": {
        "default_week_start": "monday"
    }
}
```

### Update Settings
**POST** `/settings/`
```json
{
    "default_week_start": "sunday"
}
```

### Change Password
**POST** `/settings/change-password/`
```json
{
    "old_password": "currentpassword",
    "new_password1": "newpassword123",
    "new_password2": "newpassword123"
}
```

### Delete Account
**POST** `/settings/delete-account/`
```json
{
    "confirm_delete": true,
    "password": "userpassword"
}
```

### Reset Settings
**POST** `/settings/reset-settings/`

## 👤 Accounts API

### Register User
**POST** `/accounts/signup/`
```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "password1": "securepassword123",
    "password2": "securepassword123"
}
```

### Login
**POST** `/accounts/login/`
```json
{
    "username": "johndoe",
    "password": "securepassword123"
}
```

### Logout
**POST** `/accounts/logout/`

### Update Profile
**POST** `/accounts/profile/edit/`
```
Content-Type: multipart/form-data
first_name: "John"
last_name: "Doe"
avatar: [file]
```

## 🔧 JavaScript Helpers

### Get CSRF Token
```javascript
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
```

### Make API Request
```javascript
async function makeApiRequest(url, method = 'GET', data = null) {
    const headers = {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/json',
    };
    
    const options = { method, headers };
    if (data) options.body = JSON.stringify(data);
    
    const response = await fetch(url, options);
    return await response.json();
}
```

## 📝 Response Format

### Success
```json
{
    "success": true,
    "data": {...},
    "message": "Operation completed"
}
```

### Error
```json
{
    "success": false,
    "error": "Error description"
}
```

## 🚀 Quick Test

```bash
# Start server
python manage.py runserver

# Test endpoint
curl -H "Cookie: sessionid=your-session-id" http://127.0.0.1:8000/dashboard/
```

---

**Version**: 1.0.0 | **Last Updated**: January 2024
