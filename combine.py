from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os

def convert_images_to_pdf(inputs_path, acceptable_img_file_extensions):
    image_files = []
    for file in os.listdir(inputs):
        if any([img_file_extension in file for img_file_extension in ('.jpg','.png')]):
            image_files.append(file)
    for file in image_files:
        img = Image.open(os.path.join(inputs, file))
        im1 = img.convert('RGB')
        new_filename = file[:file.find('.')]+'.pdf'
        im1.save(os.path.join(inputs, new_filename))

def clean_scanned_pdfs(inputs_path):
    pdf_files = [file for file in os.listdir(inputs) if '.pdf' in file]
    for file in pdf_files:
        pdfreadRewrite = PdfFileReader(os.path.join(inputs, file), strict = False)
        pdfwrite = PdfFileWriter()
        for page_count in range(pdfreadRewrite.numPages):
            pages = pdfreadRewrite.getPage(page_count)
            pdfwrite.addPage(pages)
        fileobjfix = open(os.path.join(inputs, file), 'wb')
        pdfwrite.write(fileobjfix)
        fileobjfix.close()

def merge_pdfs(inputs_path):
    pdf_files = [file for file in os.listdir(inputs) if '.pdf' in file]
    merger = PdfFileMerger()
    for file in pdf_files:
        merger.append(os.path.join(inputs, file))
    merger.write('Combined_Forms.pdf')
    merger.close()

if __name__ == '__main__':
    currdir = os.getcwd()
    inputs = os.path.join(currdir, 'input-docs')
    acceptable_img_file_extensions = ('.jpg','.png')
    convert_images_to_pdf(inputs, acceptable_img_file_extensions)
    clean_scanned_pdfs(inputs)
    merge_pdfs(inputs)