import os
from datetime import timedelta

class Config:
    DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'postgresql://mentalia:password@localhost/mentalia_unified'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super-secret-jwt-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
