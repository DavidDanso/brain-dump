"""
WSGI config for brain_dump project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE_PATH = CURRENT_DIR / '.env'

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brain_dump.settings')
application = get_wsgi_application()
