import os

class Config:
    # Use SQLite by default, or set a database URL in environment variables
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoid warning
    SECRET_KEY = os.urandom(24)  # Random secret key for security
