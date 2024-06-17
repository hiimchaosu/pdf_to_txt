import pymupdf

def pdf_to_txt(pdf_path, txt_path):
    pdf_document = pymupdf.open(pdf_path)
    text = ""

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)