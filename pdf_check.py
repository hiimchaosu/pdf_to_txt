import pymupdf

def check_pdf_existence(file_path):
    try:
        file = pymupdf.open(file_path)
        file.close()
        return True

    except FileNotFoundError:
        print(f"The PDF file '{file_path}' does not exist.")
        return False

    except Exception as e:
        print(f"An error occurred while trying to open '{file_path}': {e}")
        return False