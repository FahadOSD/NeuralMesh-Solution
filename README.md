# NeuralMesh - Company Website

A modern, responsive company website built with Django that showcases services, testimonials, blog posts, and contact functionality. This project provides a complete business website solution with an intuitive admin interface for content management.

## 🚀 Features

- **Responsive Design**: Modern, mobile-friendly interface using Bootstrap 5
- **Content Management**: Easy-to-use Django admin interface
- **Blog System**: Full-featured blog with authors and categories
- **Contact Form**: Email-based contact form with logging
- **Testimonials**: Customer reviews with star ratings
- **Services Showcase**: Display company services with icons
- **FAQ Section**: Frequently asked questions management
- **Rich Text Editor**: CKEditor 5 integration for blog content
- **Static File Management**: Optimized static file serving with WhiteNoise

## 🛠️ Technology Stack

- **Backend**: Django 5.1.6
- **Database**: SQLite3 (configurable for production)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Email**: SMTP (Gmail)

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd NeuralMesh-Solution-main
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📧 Email Configuration

To enable email functionality for the contact form, set up your email credentials:

1. **Set environment variable for email password**
   ```bash
   # On Windows
   set EMAIL_HOST_PASSWORD=your_app_password
   
   # On macOS/Linux
   export EMAIL_HOST_PASSWORD=your_app_password
   ```

2. **Update email settings in `company/settings.py`**
   ```python
   EMAIL_HOST_USER = 'your_email@gmail.com'
   ```


## 📁 Project Structure

```
NeuralMesh-Solution-main/
├── app/                          # Main Django application (models, views, admin)
├── company/                      # Django project settings (settings.py, urls.py)
├── static/                       # Static files (CSS, JS, images, vendor libraries)
├── templates/                    # HTML templates (pages, components)
├── staticfiles/                  # Collected static files
├── manage.py                     # Django management script
├── requirement.txt               # Python dependencies
└── README.md                    # This file
```

## 🔧 Configuration

### Environment Variables
- `EMAIL_HOST_PASSWORD`: Gmail app password for email functionality

### Settings Customization
Key settings in `company/settings.py`:
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Configure for your domain
- `DATABASES`: Configure for your database
- `STATIC_ROOT`: Static file collection directory

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Set up production database
4. Configure static file serving
5. Set up email credentials
6. Run `python manage.py collectstatic`


---
