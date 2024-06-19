import os
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pdf_check import check_pdf_existence
from pdf_to_txt import pdf_to_txt
from data_extract import extract_data

def on_drop(event):
    file_path = event.data
    # One machine had curly braces in the path, so I had to cut them out
    if file_path.startswith('{') and file_path.endswith('}'):
        file_path = file_path[1:-1]

    file_name = os.path.basename(file_path)

    if file_path.endswith(".pdf"):
        exists = check_pdf_existence(file_path)
        if exists:
            messagebox.showinfo("Result:", "Done.")
            pdf_to_txt(f"{file_name[:-4]}.pdf", f"{file_name[:-4]}.txt")
            extract_data(f"{file_name[:-4]}.txt", f"{file_name[:-4]}_edited.txt", keyword="Licznik:")
        else:
            print("The file dropped is non existent.")
            messagebox.showwarning("Warning:", "NONACCESSIBLE / NONEXISTENT")
    else:
        print("An unknown error occurred in GUI section of the code.")
        print(file_path)
        messagebox.showerror("Error:", "SOMETHING WENT WRONG. DROP PROPER .PDF FILE!")

def create_gui():
    # Creating window to drag and drop the files into
    global root
    root = TkinterDnD.Tk()
    root.title("PDF to TXT Converter - Simple Edition")
    root.geometry("400x300")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    label = tk.Label(frame, text="Choose an action:")
    label.pack(pady=5)

    merge_button = tk.Button(frame, text="Merge PDF Files", command=None)
    merge_button.pack(pady=5)

    drag_label = tk.Label(frame, text="Or drag and drop two PDF files:")
    drag_label.pack(pady=5)

    drag_button = tk.Label(frame, text="Drag-and-Drop files here", width=30, height=20, bg="lightgray")
    drag_button.pack(pady=5)
    drag_button.drop_target_register(DND_FILES)
    drag_button.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()