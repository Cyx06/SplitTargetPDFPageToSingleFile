import os

from pikepdf import Pdf
pdf = Pdf.open('input_PDF_path')   # open pdf
pages = pdf.pages                  # save each page as list
output = Pdf.new()                 # create new pdf
target_page = [1]                    # select target page, target_page 1 = pdf page 2 cuz list index start from 0
for target in target_page:
  output.pages.append(pages[target])      # add page you want to the list
output.save('output_PDF_path.pdf')             # save target pdf as new file
