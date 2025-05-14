# 🌃 DarkFolio - Personal Portfolio & Blog Template

DarkFolio is a modern, responsive Django-based portfolio and blog template with a sleek dark theme and interactive network animation background.

## ✨ Features

- 🌙 Beautiful dark theme design
- 🕸️ Interactive network animation background
- 📱 Fully responsive layout (works on all devices)
- 📝 Blog system with posts and pagination
- 🚀 Projects showcase section
- 🧑‍💼 About me page for personal info
- 👨‍💻 Admin dashboard to manage content
- 🔍 SEO-friendly structure

## 🛠️ Technologies Used

- [Django](https://www.djangoproject.com/) - Python web framework
- [Bootstrap 5](https://getbootstrap.com/) - Frontend framework
- [Font Awesome](https://fontawesome.com/) - Icons
- Vanilla JS for animations
- SQLite (default) - Database

## 📋 Requirements

- Python 3.8+ 
- Django 4.2+
- Other dependencies listed in `requirements.txt`

## 🚀 Quick Start

1. Clone the repository
```bash
git clone https://github.com/yourusername/darkfolio.git
cd darkfolio
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Load the demo data (optional)
```bash
python populate_demo.py
```

8. Open your browser and navigate to http://127.0.0.1:8000

## 💻 Admin Access

Access the admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created.

## 🎨 Customization

### Changing Basic Information

1. Log in to the admin panel
2. Update your personal information, projects, and blog posts

### Layout & Design

- CSS files are in `static/css/`
- JS files are in `static/js/`
- Templates are in `templates/`

## 🌐 Deployment

### Heroku Deployment

The project includes a `Procfile` for easy Heroku deployment:

1. Create a Heroku account and install Heroku CLI
2. Create a new app:
```bash
heroku create your-app-name
```

3. Configure environment variables:
```bash
heroku config:set SECRET_KEY=your_secret_key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

4. Deploy:
```bash
git push heroku main
```

5. Run migrations:
```bash
heroku run python manage.py migrate
```

6. Create a superuser:
```bash
heroku run python manage.py createsuperuser
```

### Other Deployment Options

The project can be deployed on any platform that supports Django, such as:

- PythonAnywhere
- AWS
- DigitalOcean
- Railway
- Render

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

If you have any questions or feedback, please reach out to me at rauljimm.dev@gmail.com or visit my website.

---

Made with ❤️ by rauljimm
