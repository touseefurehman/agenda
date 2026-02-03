# Agenda

A Django-based event management application for organizing and displaying event schedules with speakers, forums, and event details.

## Features

- **Event Management**: Create and manage events with multiple days, times, and forums
- **Speaker Management**: Add and manage speakers with photos and links
- **Event Scheduling**: Track events with start/end times and auto-calculated duration
- **Admin Dashboard**: Beautiful admin interface with Jazzmin theme
- **Image Storage**: Cloud storage integration with Cloudinary
- **Data Import/Export**: Import and export event data using django-import-export

## Tech Stack

- **Backend**: Django 6.0.1
- **Database**: SQLite (development), PostgreSQL (production)
- **Static Files**: WhiteNoise for static file handling
- **Image Storage**: Cloudinary
- **Admin UI**: Jazzmin
- **Server**: Gunicorn (production)
- **Deployment**: Railway

## Requirements

See `requirements.txt` for all dependencies. Key packages include:

- Django 6.0.1
- Pillow 12.1.0
- django-jazzmin 3.0.1
- django-cloudinary-storage 0.3.0
- cloudinary 1.44.1
- gunicorn
- psycopg2-binary
- dj-database-url

## Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:touseefurehman/agenda.git
   cd agenda
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://localhost:8000`

## Usage

### Admin Panel

Access the admin panel at `/admin/` with your superuser credentials to:
- Create and manage EventDays
- Add and edit Speakers with photos
- Create Events and assign speakers
- Configure event forums and timings

### API Endpoints

- View event schedule: `/events/schedule/`

## Project Structure

```
agenda/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── railway.toml          # Railway deployment config
├── db.sqlite3            # SQLite database (dev)
├── core/                 # Project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routing
│   ├── asgi.py           # ASGI config
│   └── wsgi.py           # WSGI config
├── events/               # Main app
│   ├── models.py         # Database models
│   ├── views.py          # Views and logic
│   ├── urls.py           # App URL patterns
│   ├── admin.py          # Admin configuration
│   └── migrations/       # Database migrations
├── templates/            # HTML templates
│   └── events/
│       └── schedule.html # Event schedule template
├── static/               # Static files (images, etc)
└── staticfiles/          # Collected static files
```

## Database Models

### EventDay
Represents a single day of events with title, details, and date.

### Speaker
Represents a speaker with:
- Name
- Designation
- Organization
- Photo (stored on Cloudinary)
- Link (URL to speaker profile/website)

### Event
Represents an event scheduled on a specific EventDay with:
- Title
- Start and end times
- Auto-calculated duration
- Forum information
- Multiple associated speakers

## Configuration

### Environment Variables

For production deployment, configure:
- `DEBUG`: Set to `False` in production
- `CLOUDINARY_URL`: Your Cloudinary API credentials
- `DATABASE_URL`: Database connection string (PostgreSQL in production)
- `SECRET_KEY`: Django secret key

### Django Settings

Key settings in `core/settings.py`:
- `INSTALLED_APPS`: Includes Jazzmin, events app, and import/export
- `MIDDLEWARE`: Includes security, sessions, and WhiteNoise for static files
- `ALLOWED_HOSTS`: Configure for your domain

## Deployment

The application is configured for deployment on Railway using `railway.toml`. It uses:
- Gunicorn as the application server
- PostgreSQL for the database
- Cloudinary for image storage
- WhiteNoise for static file serving

## Development

### Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect static files
```bash
python manage.py collectstatic --noinput
```

### Run tests
```bash
python manage.py test
```

## License

This project is part of the Agenda application ecosystem.

## Contributing

For contributions, please maintain the existing code structure and add appropriate migrations for any model changes.

## Support

For issues or questions, please refer to the project repository or contact the maintainer.
