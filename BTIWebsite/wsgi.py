import os
import sys


project_home = '/home/ValeriyaM/BTI-Center-for-Expertise-and-Inventory'
if project_home not in sys.path:
    sys.path.insert(0, project_home)


activate_this = '/home/ValeriyaM/BTI-Center-for-Expertise-and-Inventory/venv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BTIWebsite.settings')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
