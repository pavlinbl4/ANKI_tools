import openpyxl
from remove_tags import cleanhtml


def read_data(xlsx_file):
    file_data = openpyxl.load_workbook(xlsx_file)
    return file_data


def get_sheet_names(xlsx_file_data):
    return xlsx_file_data.sheetnames


def find_specific_cell(current_sheet):
    for row in range(8, current_sheet.max_row + 1):
        for column in "CD":  # Here you can add or reduce the columns
            cell_name: str = "{}{}".format(column, row)
            if current_sheet[cell_name].value is not None:
                if "<" in current_sheet[cell_name].value:
                    # print("cell position {} has value {}".format(cell_name, current_sheet[cell_name].value))
                    clean_value = cleanhtml(current_sheet[cell_name].value)
                    print(clean_value)
                    current_sheet[cell_name].value = clean_value





anki_excel_file = '/Volumes/big4photo/Documents/ANKI/english_words.xlsx'

if __name__ == '__main__':
    xlsx_file_data = read_data(anki_excel_file)
    sheet_names = get_sheet_names(xlsx_file_data)
    current_sheet = xlsx_file_data[sheet_names[0]]
    find_specific_cell(current_sheet)
    xlsx_file_data.save('/Volumes/big4photo/Documents/ANKI/free_from_tags.xlsx')


    # print(current_sheet['B8'].value)
