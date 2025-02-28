import logging
from typing import Any
from celery import shared_task
from django.db import transaction

from main.google_sheets import GoogleSheet

logger: logging.Logger = logging.getLogger(__name__)


@shared_task
@transaction.atomic
def get_drivers() -> dict[str, Any]:
    """Получает водителей из таблицы и записывает в БД."""
    try:
        return GoogleSheet.get_data()
    except Exception as e:
        logger.error("Произошла ошибка при выполнении задачи: %s", str(e))
        return {"error": str(e)}
