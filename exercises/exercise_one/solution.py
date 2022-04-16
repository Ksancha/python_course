import os


def get_list_of_files():
    return os.listdir()


# Create a function get_pdf_files

def get_pdf_files():
    files = get_list_of_files()
    result = []
    for i in files:
        if i[-3:] == "pdf":
            result.append(i)
    return result

# Create a function get_csv_files


def get_csv_files():
    files = get_list_of_files()
    result_csv = []
    for i in files:
        if i[-3:] == "csv":
            result_csv.append(i)
    return result_csv


# Create a function get_jpg_files

def get_jpg_files():
    files = get_list_of_files()
    result = []
    for i in files:
        if i[-3:] == "jpg":
            result.append(i)
    return result


# Create a single function get_files_by_extension

def get_files_by_extension(extension):
    result = []
    for i in get_list_of_files():
        if i[-len(extension):] == extension:
            result.append(i)
    return result


print(get_files_by_extension(extension="py"))