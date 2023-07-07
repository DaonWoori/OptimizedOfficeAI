"""
WSGI config for Review_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# wsgi.py: WSGI(Web Server Gateway Interface) 서버와 Django 애플리케이션 간의 연결을 담당하는 역할을 수행
# -> wsgi.py 파일은 Django 애플리케이션을 WSGI 서버에 연결하는 역할을 하며, 웹 서버와 Django 애플리케이션 간의 상호작용을 중개함 

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Review_site.settings')

application = get_wsgi_application()
