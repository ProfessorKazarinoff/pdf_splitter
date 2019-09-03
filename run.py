# run.py
"""
 # create Python 3 virtual env
 > pip install -r requirements.txt
 > python run.py

A GUI that pulls out specific pdf pages into another pdf document
"""

from pathlib import Path
from PyPDF4 import PdfFileReader, PdfFileWriter
from gooey import Gooey, GooeyParser

def pdf_splitter(in_path: Path, out_path: Path, page_list: list):
    """
    A function to split a pdf into different pages
    """
    f = open(in_path, 'rb')
    pdf = PdfFileReader(f)
    pdf_writer = PdfFileWriter
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

@Gooey()
def main():
    desc = "A Python Gooey App to extract pdf pages"
    pdf_select_help_message = "Select a .pdf file to pull pages out of"
    parser = GooeyParser(description=desc)
    parser.add_argument(
        "PDF_to_extract_from", help=pdf_select_help_message, widget="FileChooser")
    parser.add_argument("Output_Directory", help="Directory to save output", widget="DirChooser")
    parser.add_argument("Output_File", help="Output file name", widget="TextField")
    parser.add_argument("Page_List", help="List of pagex to extract", widget="TextField")
    args = parser.parse_args()

    outfile_Path = Path(args.Output_Directory, Path(args.Output_File))
    in_Path = Path(args.PDF_to_extract_from)
    list_str = str(args.Page_List)

    p_list = string_to_list(list_str)
    pdf_splitter(in_Path, outfile_Path, p_list)


if __name__ == "__main__":
    main()
