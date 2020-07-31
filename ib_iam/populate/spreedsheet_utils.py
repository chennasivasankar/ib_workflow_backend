import gspread


class SpreadSheetUtil:
    def __init__(self):
        scope = [
            "https://www.googleapis.com/auth/drive",
            "https://spreadsheets.google.com/feeds",
        ]

        from oauth2client.service_account import ServiceAccountCredentials
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "ib_iam/populate/ib-worksflows-dev-testing-d86743f0ecd1.json",
            scope)

        self.gc = gspread.authorize(credentials)

    def read_spread_sheet_data_and_get_row_wise_dicts(
            self, spread_sheet_name, sub_sheet_name):
        wks = self.gc.open(spread_sheet_name).worksheet(sub_sheet_name)
        spread_sheet_data = wks.get_all_values()

        headers = spread_sheet_data[0]
        headers = [header.strip() for header in headers]

        row_wise_dicts = []
        row = 1
        while row < len(spread_sheet_data):
            data = spread_sheet_data[row]

            row_wise_dict = dict()
            for index, key in enumerate(headers):
                row_wise_dict[key] = data[index].strip()
            row_wise_dicts.append(row_wise_dict)

            row += 1

        return row_wise_dicts
