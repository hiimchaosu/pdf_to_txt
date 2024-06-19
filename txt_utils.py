import os

def merge_txt_files(txt_file1, txt_file2, output_file):
    try:
        with open(txt_file1, 'r', encoding='utf-8') as file1:
            text1 = file1.read()
        with open(txt_file2, 'r', encoding='utf-8') as file2:
            text2 = file2.read()
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(text1 + "\n" + text2)
    except Exception as e:
        print(f"Error merging text files: {e}")

def delete_files(*file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")