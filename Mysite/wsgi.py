"""
WSGI config for Mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application

"""
Add by han yaguang,why? I don't know yet
"""
import sys
sys.path.append("/home/Mysite")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mysite.settings")

application = get_wsgi_application()
