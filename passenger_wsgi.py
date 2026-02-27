"""
Punto de entrada para cPanel Python Selector (Passenger/WSGI).
Este archivo es requerido por cPanel para ejecutar la aplicación Django.
"""
import sys
import os
import pymysql
pymysql.install_as_MySQLdb()

# Agrega el directorio del proyecto al path de Python
sys.path.insert(0, os.path.dirname(__file__))

# Módulo de configuración Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
