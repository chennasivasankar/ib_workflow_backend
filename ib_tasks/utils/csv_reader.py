import csv
from collections import defaultdict
from itertools import zip_longest
from typing import List, Dict


def read_csv_file(file_path: str) -> List[Dict]:
    """
        this function takes a file path of a csv file
        and returns a list of dicts in the format below
            [
                {
                    "col_header1": "first row val for this col",
                    "col_header2": "first row val for this col",
                    "col_header3": "first row val for this col",
                    .... up to no of cols you have in your excel sheet
                },
                {
                    "col_header1": "second row val for this col",
                    "col_header2": "second row val for this col",
                    "col_header3": "second row val for this col",
                    .... up to no of cols you have in your excel sheet
                },
                ..... up to no of rows in your excel sheet
            ]
        if you do not understand the above part, print the result yourself and
        you will get it... :)
        NOTE: you will have to make sure your excel sheet is clean and having
        all the required values when exporting as csv file, otherwise,
        you will get some unexpected results from this function.
    """
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        col_headers = csv_reader.__next__()
        col_headers = remove_stars_in_the_end(col_headers=col_headers)
        result = []
        for row in csv_reader:
            row_dict = defaultdict()
            for col_header, col_val in zip_longest(col_headers, row):
                row_dict[col_header] = col_val
            result.append(row_dict)
        return result


def remove_stars_in_the_end(col_headers: List[str]) -> List[str]:
    reformatted_col_headers = []
    for col_header in col_headers:
        if col_header[-1] == "*":
            reformatted_col_headers.append(col_header[:-1])
        else:
            reformatted_col_headers.append(col_header)
    return reformatted_col_headers
