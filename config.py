# ============================================
# EduTrackX — Configuration
# Student Result Management System
# ============================================

import os


class Config:
    """Base configuration class."""

    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY', 'edutrackx-secret-key-change-in-production-2026')
    DEBUG = True

    # MySQL Database
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Jantyking@1')  # <--- DB PASSWORD
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'edutrackx')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', None)  # Must be set in production


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


# Active configuration
active_config = DevelopmentConfig()
