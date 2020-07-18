from gspread.models import Spreadsheet


def read_google_sheet(sheet_name: str) -> Spreadsheet:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = [
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '/home/ib-developer/Desktop/aws/ib-workflows-backend/ib_tasks/utils'
        '/workflow-types-4f1e079f438e.json', scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet
