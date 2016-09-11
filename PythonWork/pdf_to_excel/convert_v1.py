#!/usr/bin/python
# -*- coding: utf-8 -*-

# from pdfminer.pdfinterp import PDFResourceManager,process_pdf 
from pdfminer.converter import TextConverter 
from pdfminer.layout import LAParams 
from io import StringIO



def main():

    res=convert_pdf_to_txt("f1.pdf")
    print res
    # print convert_pdf_to_txt("f1.pdf")
    # convert_pdf_to_txt2("f1.pdf")
    # print(convert_pdf('f1.pdf', page=1))


def pdf_to_excel(file):
    pass




from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,password=password,caching=caching, check_extractable=True):

        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def convert_pdf_to_txt2(filename):
    import pyPdf
    pdf = pyPdf.PdfFileReader(open(filename, "rb"))
    for page in pdf.pages:
        print page.extractText()

def convert_pdf(path, page=1): 
    rsrcmgr = PDFResourceManager() 
    retstr = StringIO() 
    laparams = LAParams() 
    device = TextConverter(rsrcmgr, retstr, pageno=page, laparams=laparams) 
    fp = open(path, 'rb') 
    process_pdf(rsrcmgr, device, fp) 
    fp.close() 
    device.close() 
    str = retstr.getvalue()

    retstr.close() 
    return str








if __name__ == '__main__':
    main()