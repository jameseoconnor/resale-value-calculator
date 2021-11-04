"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

load_dotenv()
env =  os.getenv('ENV')

if env=="PROD":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.prod_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.dev_settings')

application = get_wsgi_application()
