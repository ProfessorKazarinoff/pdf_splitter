# run.py
"""
 # create Python 3 virtual env
 > pip install -r requirements.txt
 > python run.py

A GUI that pulls out specific pdf pages into another pdf document
"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(in_path: Path, out_path: Path, page_list: list):
    """
    A function to split a pdf into different pages
    """
    pdf = PdfFileReader(in_path)
    pdf_writer = PdfFileWriter
    #page_list = [1, 4, 5]
    pdf_writer = PdfFileWriter()
    for page in page_list:
        pdf_writer.addPage(pdf.getPage(page-1))
    with open(out_path, "wb") as out:
        pdf_writer.write(out)


def string_to_list(in_str):
    """
    a function to break a comma-seperated string into a list of integers
    """
    out_lst = [int(s.strip()) for s in in_str.split(",")]
    return out_lst


def main():
    print("Relative to the cwd, what is the .pdf input filename?")
    f_name_in = input("Enter input pdf file name: ")
    print("Relative to the cwd, what is the .pdf output filename?")
    f_name_out = input("Enter output pdf file name: ")
    print("Which pages do you want to extract into a new file?")
    list_str = input("Enter list of pages seperated with a comma: ")

    cwd = Path.cwd()
    f_in = Path(f_name_in)
    f_out = Path(cwd, f_name_out)
    p_list = string_to_list(list_str)
    pdf_splitter(f_name_in, f_out, p_list)


if __name__ == "__main__":
    main()
