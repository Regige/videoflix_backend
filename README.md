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
   python3 -m venv env
   source env/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
   
4. **Install FFmpeg**:
   
   FFmpeg is required for processing video files. Follow the [official installation guide](https://ffmpeg.org/download.html) to install FFmpeg on your system.
    
5. **Install PostgreSQL**:
   
   This project uses PostgreSQL as the default database. Install PostgreSQL by following the instructions for your operating system on the [official PostgreSQL website](https://www.postgresql.org/download).
   After installation:
   - Create a new PostgreSQL database.
   - Update your `settings.py` with the database credentials.
     
6. **Alternative: Use SQLite**:

   If you prefer, you can use SQLite instead of PostgreSQL. The configuration for SQLite is already included in `settings.py`, but it is commented out. Uncomment the SQLite settings and comment out the PostgreSQL settings to switch.
   
7. **Set up environment variables**:
   Create a `.env` file in the root directory with the following variables:

   ```dotenv
   SECRET_KEY=MY_SECRET_KEY
   REDIS_USER=your_redis_username
   REDIS_PASSWORD=your_redis_password
   EMAIL_HOST=your_host.com
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_KEY=your_email_password_or_app_key
   DATABASE_NAME=your_postgres_db_name
   DATABASE_USER=your_postgres_user
   DATABASE_PASSWORD=your_postgres_password
   DATABASE_HOST=your_postgres_host
   DATABASE_PORT=your_postgres_port
   ```

8. **Apply migrations and run the development server**:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

7. **Start the Redis worker**:
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

- **Database**:
   - The project uses PostgreSQL by default. Update the database credentials in `.env` and `settings.py`.
   - To use SQLite instead, modify `settings.py` as described in the installation section.
- **Cache**: Configured with Redis.
- **Authentication**: JWT-based, with access and refresh token lifetimes set in `SIMPLE_JWT`.
- **Email**: Configured to use Gmail's SMTP service for email functionalities like password resets.
- **Video Processing**: Requires FFmpeg to process and manage video files.

## Dependencies

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

This project was created with Python version 3.9.6. Ensure you are using this version or a compatible one.

## Documentation

- Further details on Django settings can be found in the [official Django documentation](https://docs.djangoproject.com/en/4.2/topics/settings/).
- For Django Rest Framework, visit [DRF documentation](https://www.django-rest-framework.org/).
- Learn more about PostgreSQL from the [official PostgreSQL website](https://www.postgresql.org/download).

## Troubleshooting

- **CORS issues**: Ensure the frontend's origin is listed in `CORS_ALLOWED_ORIGINS`.
- **Database Errors**:
   - Make sure migrations are applied correctly.
   - Ensure the correct database credentials are set in `.env`.
- **Redis Connection**: Verify Redis is running and accessible with the correct credentials.
- **FFmpeg Errors**: Ensure FFmpeg is installed and added to your system's PATH.

## Contributors

- **Regina Gering** - [Your GitHub](https://github.com/Regige)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
