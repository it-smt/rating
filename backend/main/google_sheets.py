from collections import Counter
import logging
from typing import Any

from django.conf import settings
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from main.models import People, Rank
from main.services.people_service import PeopleService
from main.services.rank_service import RankService


logger: logging.Logger = logging.getLogger(__name__)


class GoogleSheet:
    """Класс для работы с Google Sheets."""

    @staticmethod
    def get_data() -> dict[str, int]:
        """Возвращает данные людей."""
        client: gspread.Client = GoogleSheet._get_google_sheet_client()
        sheet: gspread.Worksheet = client.open(settings.GOOGLE_SHEET_NAME).sheet1

        peoples: dict[str, int] = GoogleSheet._get_peoples_from_table(sheet)
        logger.info("Данные из Google Sheets успешно получены: %s", peoples)
        return peoples

    @staticmethod
    def _get_peoples_from_table(sheet: gspread.Worksheet) -> dict[str, int]:
        """Добавление людей в БД."""
        call_signs: list[str] = GoogleSheet._fetch_call_signs(sheet)
        call_sign_counts: dict[str, int] = GoogleSheet._process_call_signs(call_signs)

        PeopleService.bulk_update_or_create(call_sign_counts)

        return call_sign_counts

    @staticmethod
    def _get_google_sheet_client() -> gspread.Client:
        """Авторизация и получение клиента Google Sheets."""
        try:
            credentials: ServiceAccountCredentials = (
                ServiceAccountCredentials.from_json_keyfile_name(
                    settings.GOOGLE_SHEET_CREDENTIALS_FILE_NAME,
                    settings.GOOGLE_SHEETS_SCOPE,
                )
            )
            return gspread.authorize(credentials)
        except Exception as e:
            logger.error("Ошибка при авторизации в Google Sheets: %s", str(e))
            raise

    @staticmethod
    def _fetch_call_signs(sheet: gspread.Worksheet) -> list[str]:
        """Получение списка позывных из Google Sheets."""
        try:
            all_values: list[Any] = sheet.col_values(1)
            return all_values[1:]  # Пропускаем заголовок
        except Exception as e:
            logger.error("Ошибка при получении данных из Google Sheets: %s", str(e))
            raise

    @staticmethod
    def _process_call_signs(call_signs: list[str]) -> dict[str, int]:
        """Подсчет количества повторений каждого позывного."""
        return dict(Counter(call_signs))
