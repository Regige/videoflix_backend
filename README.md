# Videoflix

## Introduction

**Videoflix** is the backend for a video platform, created as a learning project to gain deeper insights into Django, especially Django Rest Framework. This repository contains the database and the REST API that handles all requests from the frontend. The frontend is built with Angular, and it is separate from the backend. You can find it publicly available on my GitHub profile.

## Features

- **REST API**: A comprehensive REST API is defined to manage requests such as user registration and login using JWT authentication.
- **Video Management**: The API allows querying all videos stored in the database.
- **Password Reset**: An endpoint is provided for resetting user passwords.

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd videoflix
   ```

2. **Create a virtual environment**:

   It is recommended to use Python version 3.9.6 to ensure compatibility:
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory with the following variables:

   ```dotenv
   SECRET_KEY=MY_SECRET_KEY
   REDIS_USER=your_redis_username
   REDIS_PASSWORD=your_redis_password
   EMAIL_HOST=your_host.com
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_KEY=your_email_password_or_app_key
   ```

5. **Apply migrations and run the development server**:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. **Start the Redis worker**:
   Ensure that the `redis-server` is running:

   ```bash
   redis-server
   ```

   Open redis cli and setup username and password in redis:

   ```bash
   redis-cli
   ACL SETUSER your_username on >your_password ~* +@all
   ```

   Then start the RQ worker:

   ```bash
   python manage.py rqworker
   ```

## Usage

- The backend is primarily interacted with through its REST API.
- Example endpoints:
  - **User Registration/Login**: `POST /accounts/`, `POST /accounts/api/token/`
  - **Fetch Videos**: `GET /videos/all/`
  - **Password Reset**: `POST /accounts/password_reset/`

## Configuration

- **Database**: Uses SQLite by default, configured in `settings.py`.
- **Cache**: Configured with Redis.
- **Authentication**: JWT-based, with access and refresh token lifetimes set in `SIMPLE_JWT`.
- **Email**: Configured to use Gmail's SMTP service for email functionalities like password resets.

## Dependencies

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

This project was created with Python version 3.9.6. Ensure you are using this version or a compatible one.

## Documentation

- Further details on Django settings can be found in the [official Django documentation](https://docs.djangoproject.com/en/4.2/topics/settings/).
- For Django Rest Framework, visit [DRF documentation](https://www.django-rest-framework.org/).

## Troubleshooting

- **CORS issues**: Ensure the frontend's origin is listed in `CORS_ALLOWED_ORIGINS`.
- **Database Errors**: Make sure migrations are applied correctly.
- **Redis Connection**: Verify Redis is running and accessible with the correct credentials.

## Contributors

- **Regina Gering** - [Your GitHub](https://github.com/Regige)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
