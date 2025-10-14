import os
import sys

# шлях до проєкту
path = '/home/ValeriyaM/BTI-Center-for-Expertise-and-Inventory'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'BTIWebsite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
