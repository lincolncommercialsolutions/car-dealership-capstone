"""
WSGI config for dealership project.
"""

import os

from django.core.wsgi import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealership.settings')

application = application()
