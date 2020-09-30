"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""

from gspread.models import Spreadsheet


def read_google_sheet(sheet_name: str) -> Spreadsheet:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = [
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        './ib-workflows-9f437d357f89.json', scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet
