# Django settings for octofit_tracker project

INSTALLED_APPS = [
    # ...existing apps...
    'corsheaders',
    'octofit',
    'octofit_tracker',  # Added the octofit_tracker app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        },
    }
}

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
