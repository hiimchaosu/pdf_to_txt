import os
import tkinter as tk
import datetime
import locale
import webbrowser
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pdf_to_txt import pdf_to_txt
from data_extract import extract_data
from txt_utils import merge_txt_files, delete_files

files_converted = 0
file1 = ""
file2 = ""
pathFile1 = ""
pathFile2 = ""
locale.setlocale(locale.LC_TIME, "pl_PL.UTF-8")

def callback(url):
    webbrowser.open_new_tab(url)

def on_drop(event):
    file_path = event.data
    global files_converted
    global file1
    global file2
    global pathFile1
    global pathFile2
    getDate = datetime.datetime.now()
    getDateMonth = getDate.strftime("%B")
    getDateYear = getDate.strftime("%Y")
    print(f"Year: {getDateYear}")
    print(f"Month: {getDateMonth}")

    # One machine had curly braces in the path, so I had to cut them out
    if file_path.startswith('{') and file_path.endswith('}'):
        file_path = file_path[1:-1]

    file_name = os.path.basename(file_path)

    if file_path.endswith(".pdf"):
        files_converted = files_converted + 1
        messagebox.showinfo("Result:", "Done.")
        pdf_to_txt(f"{file_name[:-4]}.pdf", f"{file_name[:-4]}.txt")
        extract_data(f"{file_name[:-4]}.txt", f"{file_name[:-4]}_edited.txt", keyword="Licznik:")
        if files_converted == 1:
            file1 = file_name[:-4]
            pathFile1 = file_path
            print(f"File1: {file1}")
            print(f"pathFile1: {pathFile1[:-4]}")
        else:
            if file_name[:-4] == file1:
                messagebox.showwarning("Duplicate:", "You have put the same file twice.")
                files_converted = 1
            else:
                file2 = file_name[:-4]
                pathFile2 = file_path
                print(f"File2: {file2}")
                print(f"pathFile2: {pathFile2}")
                merge_txt_files(f"{file1}_edited.txt", f"{file2}_edited.txt", f"KG Liczniki {getDateMonth} {getDateYear}_merged.txt")
                delete_files(f"{pathFile1[:-4]}_edited.txt", f"{pathFile2[:-4]}_edited.txt", f"{pathFile1[:-4]}.txt", f"{pathFile2[:-4]}.txt")
                files_converted = 0
    else:
        print("The file dropped is non existent or is of invalid type.")
        messagebox.showwarning("Warning:", "INVALID TYPE / NONEXISTENT")

def create_gui():
    # Creating window to drag and drop the files into
    global root
    root = TkinterDnD.Tk()
    root.title("PDF2TXT Convert and Merge - Simple Edition")
    root.geometry("400x300")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    label = tk.Label(frame, text="Coded by: hiimchaosu", fg="blue", cursor="hand2")
    label.pack(pady=5)
    label.bind("<Button-1>", lambda e: callback("https://github.com/hiimchaosu/"))

    drag_button = tk.Label(frame, text="Drag-and-Drop files here", width=30, height=20, bg="lightgray")
    drag_button.pack(pady=5)
    drag_button.drop_target_register(DND_FILES)
    drag_button.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()

# TODO - Maybe convert data into a simple class and use it this way? -> "File: id1 name1 path1" etc. but that will be done... later... for now, rough sketch of the program is done :D
# P.S. There are still some console prints, that are there for me to troubleshoot if needed