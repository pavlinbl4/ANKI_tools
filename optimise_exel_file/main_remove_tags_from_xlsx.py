import openpyxl
from remove_tags import cleanhtml
from tkinter import filedialog, messagebox
import os
from pathlib import Path


def read_data(xlsx_file):
    file_data = openpyxl.load_workbook(xlsx_file)
    return file_data


def get_sheet_names(xlsx_file_data):
    return xlsx_file_data.sheetnames


def find_specific_cell(current_sheet, columns_for_edit):
    for row in range(8, current_sheet.max_row + 1):
        for column in columns_for_edit:  # Here you can add or reduce the columns
            cell_name: str = "{}{}".format(column, row)
            if current_sheet[cell_name].value is not None:
                # if "<" in current_sheet[cell_name].value:
                # print("cell position {} has value {}".format(cell_name, current_sheet[cell_name].value))
                clean_value = cleanhtml(current_sheet[cell_name].value).strip()
                print(clean_value)
                current_sheet[cell_name].value = clean_value


def clear_cells_from_html(input_xlsx_file, columns_for_edit):
    file_name = get_filename(anki_excel_file)
    xlsx_file_data = read_data(anki_excel_file)
    sheet_names = get_sheet_names(xlsx_file_data)
    current_sheet = xlsx_file_data[sheet_names[0]]
    find_specific_cell(current_sheet, columns_for_edit)
    xlsx_file_data.save(anki_excel_file)

    messagebox.showinfo(title="All done", message=f'file {file_name}_cleared.xlsx \ncreated')


def select_file():  # return path to the file
    return filedialog.askopenfilename(initialdir=f'{Path().home()}/Documents/ANKI/', defaultextension='xlsx')


def get_filename(file_path):
    return os.path.basename(file_path).split('.')[0]


def read_selected_column(anki_excel_file):
    xlsx_file_data = read_data(anki_excel_file)
    sheet_names = get_sheet_names(xlsx_file_data)
    current_sheet = xlsx_file_data[sheet_names[0]]

    column_index = 7

    for row in current_sheet.iter_rows():
        cell_value = row[column_index - 1].value
        if cell_value is not None:
            print(cell_value)


if __name__ == '__main__':
    anki_excel_file = f'{Path().home()}/Documents/ANKI/ANKI_EXCEL.xlsx'
    columns = "DEG"
    clear_cells_from_html(anki_excel_file, columns)
