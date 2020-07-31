from gspread.models import Spreadsheet


def get_google_sheet(sheet_name: str) -> Spreadsheet:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = [
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'ib_tasks/utils/ib-worksflows-dev-testing-d86743f0ecd1.json', scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name)
    return sheet