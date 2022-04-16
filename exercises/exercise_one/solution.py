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

# Create a function get_jpg_files

# Create a single function get_files_by_extension
