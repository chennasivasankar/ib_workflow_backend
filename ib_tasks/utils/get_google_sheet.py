
import gspread
from oauth2client.service_account import ServiceAccountCredentials



def get_google_sheet():
    scope = [
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'ib_tasks/utils/workflow-types-4f1e079f438e.json', scope
    )
    client = gspread.authorize(creds)
    sheet = client.open('FinMan Configuration Rajesh')
    return sheet
