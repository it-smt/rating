import re
from collections import Counter
from typing import Any

from celery import shared_task
from django.conf import settings
from django.db import transaction

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from main.models import People, Rank


@shared_task
@transaction.atomic
def fetch_call_signs_and_save_to_db() -> None:
    try:
        CREDENTIALS_FILE = f"{settings.BASE_DIR}/credentials.json"

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE, scope
        )

        client = gspread.authorize(credentials)

        sheet = client.open("test").sheet1
        all_values: Any = sheet.col_values(1)
        call_signs: Any = all_values[1:]

        def is_valid_call_sign(call_sign):
            return re.match(r"^[А-Я]", call_sign) is not None

        valid_call_signs = [
            sign.strip() for sign in call_signs if is_valid_call_sign(sign.strip())
        ]
        call_sign_counts: list[dict] = Counter(valid_call_signs)
        rank = Rank.objects.get(title="Бронза")
        if rank:
            People.objects.all().delete()
            for call_sign, count in call_sign_counts.items():
                People.objects.create(
                    call_sign=call_sign, orders_count=count, rank=rank
                )

            return call_sign_counts
        return {"msg": "У вас нет базового ранга 'Бронза'"}
    except Exception as e:
        return {"error": str(e)}
