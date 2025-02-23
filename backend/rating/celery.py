import os
from celery import Celery

# from celery.signals import worker_ready
# from main.tasks import fetch_call_signs_and_save_to_db

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rating.settings")

app = Celery("rating")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


# @worker_ready.connect
# def at_start(sender, **kwargs) -> None:
#     with sender.app.connection():
#         fetch_call_signs_and_save_to_db.delay()
