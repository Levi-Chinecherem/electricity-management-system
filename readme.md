# Electricity Management System

The Electricity Management System is a web-based expert electricity metering, billing, and control system developed using Django, jQuery Ajax, and Bootstrap 4.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

1. **User Authentication:** Allows users to sign up, log in, log out, and change passwords.
2. **Consumer Management:** Users can add consumers, specifying consumer type and associated appliances.
3. **Consumption Tracking:** Tracks and displays the consumption units of consumers.
4. **Demand Requests:** Enables users to send demand requests.
5. **Billing System:** Generates monthly bills based on consumption units and calculates the total amount.
6. **Power Control:** Allows users to control appliances associated with consumers.

## Requirements

- Python 3.x
- Django 3.x
- MySQL (or any other supported database)
- Web browser with JavaScript enabled

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/electricity-management-system.git
   cd electricity-management-system
   ```
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Create and apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:

   ```bash
   python manage.py runserver
   ```
8. Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in with the superuser credentials.

## Configuration

- **Database Configuration:** Update the `DATABASES` setting in `settings.py` to use your preferred database.
- **Static Files:** Run the following command to collect static files:

  ```bash
  python manage.py collectstatic
  ```
- **Django Settings:** Customize other settings in the `settings.py` file as needed.

## Usage

1. Log in to the admin panel using the superuser credentials.
2. Add consumers, specify consumer type, and associated appliances.
3. Explore the different functionalities such as viewing consumption, sending demand requests, viewing billing, and controlling appliances.

## Directory Structure

electricity_management_system/
├── accounts/           # User authentication app
├── home/               # Home app
├── electricity_management/  # Main app for the electricity management system
│   ├── migrations/     # Database migrations
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py       # Database models
│   ├── tests.py
│   ├── urls.py         # URL patterns
│   └── views.py        # Views and business logic
├── venv/               # Virtual environment
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies

```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add my feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
