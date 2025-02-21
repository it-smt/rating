import os
from django.conf import settings
import gspread
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = "path/to/your/credentials.json"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]


def get_gspread_client() -> gspread.Client:
    token_file = "token.json"
    if os.path.exists(token_file):
        credentials: ServiceAccountCredentials = (
            ServiceAccountCredentials.from_json_keyfile_name(token_file, scope)
        )
    else:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE, scope
        )
        with open(f"{settings.BASE_DIR}/token.json", "w", encoding="utf-8") as f:
            f.write(credentials.to_json())

    return gspread.authorize(credentials)
