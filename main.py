from PyPDF2 import PdfWriter, PdfReader
from tqdm import tqdm
from os import listdir
from os.path import isdir, join
import argparse

parser = argparse.ArgumentParser(description='Process PDF file!')
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()

path_to_root = args.path
print("\n##################################")
print("Bat dau xu ly cho cac thu muc nam trong:", path_to_root)
ls_dir = listdir(path_to_root)

count = 0
for directory in tqdm(ls_dir):
    path_to_dir = join(path_to_root, directory)
    if isdir(path_to_dir):
        ls_file = listdir(path_to_dir)
        ls_pdf = [f for f in ls_file if ".pdf" in f]
        if len(ls_pdf) != 1:
            continue
        else:
            path_pdf = join(path_to_dir, ls_pdf[0])
            with open(path_pdf, "rb") as infile:
                reader = PdfReader(infile)
                pdfObj = reader.pages
                if len(pdfObj) > 2:
                    writer_1 = PdfWriter()
                    writer_1.add_page(pdfObj[0])
                    writer_1.add_page(pdfObj[1])
                    path_pdf_1 = join(path_to_dir, "GCN.pdf")
                    with open(path_pdf_1, "wb") as GCN:
                        writer_1.write(GCN)

                    writer_2 = PdfWriter()
                    for page in pdfObj[2:]:
                        writer_2.add_page(page)
                    path_pdf_2 = join(path_to_dir, "other.pdf")
                    with open(path_pdf_2, "wb") as other:
                        writer_2.write(other)

                    count += 1

print(f"Hoan thanh xu ly tach file PDF thanh cong cho {count} thu muc!")
print("##################################\n")
