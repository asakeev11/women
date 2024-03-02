import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitewomen.settings')


app = Celery('sitewomen')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'send-spam': {
#         'task': 'sitewomen.tasks.send_email',
#         'schedule': 30.00,
#     }
# }