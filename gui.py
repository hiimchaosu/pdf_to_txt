import os
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pdf_check import check_pdf_existence
from pdf_to_txt import pdf_to_txt
from data_extract import extract_data

def on_drop(event):
    file_path = event.data
    file_name = os.path.basename(file_path)
    if file_path.endswith(".pdf"):
        exists = check_pdf_existence(file_path)
        if exists:
            messagebox.showinfo("Result:", "ACCESSIBLE")
            pdf_to_txt(f"{file_name[:-4]}.pdf", f"{file_name[:-4]}.txt")
            extract_data(f"{file_name[:-4]}.txt", f"{file_name[:-4]}_edited.txt", keyword="Licznik:")
        else:
            messagebox.showwarning("Warning:", "NONACCESSIBLE / NONEXISTENT")
    else:
        messagebox.showerror("Error:", "SOMETHING WENT WRONG. DROP PROPER .PDF FILE!")

def create_gui():
    # Creating window to drag and drop the files into
    root = TkinterDnD.Tk()
    root.title("PDF to TXT Converter - Simple Edition")
    root.geometry("400x200")

    label = tk.Label(root, text="Drag and drop a PDF file here", width=40, height=10, bg="lightgray")
    label.pack(pady=20)

    # Bind the drop event to the on_drop function
    label.drop_target_register(DND_FILES)
    label.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()