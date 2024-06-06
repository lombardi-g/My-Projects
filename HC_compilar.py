from openpyxl import load_workbook

compiled_file = "HC_compilado.xlsx"
raw_file = "..."

destination_workbook = load_workbook(compiled_file)
destination_sheet = destination_workbook.active

raw_workbook = load_workbook(raw_file)
raw_sheet = raw_workbook.active

def read_raw_HC():
    raw_headers = []
    correct_headers = []
    exported_headers = []
    for _ in 27:
        exported_headers.append(None)
    for cell in raw_sheet[1]:
        raw_headers.append(cell.value)
    for cell in destination_sheet[1]:
        correct_headers.append(cell)
    for value in raw_headers:
        for header in correct_headers:
            if value == header:
                exported_headers[header.index()] = value

raw_headers = []

def write_compiled_HC():
    ...
read_raw_HC()
