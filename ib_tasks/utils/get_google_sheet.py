import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_google_sheet():
    scope = [
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'ib_tasks/utils/google_sheets_credentials.json', scope
    )
    client = gspread.authorize(creds)
    sheet = client.open('FinMan Configuration_Dev_Test')
    return sheet
