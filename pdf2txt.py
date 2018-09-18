import os
import PyPDF2
#from pyPDF2 import pdfFileReader
from PyPDF2 import PdfFileReader, PdfFileWriter

def getTextPDF(pdfFileName,password=''):
	    pdf_file=open(pdfFileName,'rb')
	    read_pdf=PyPDF2.PdfFileReader(pdf_file)
	    if password !='':
	    	read_pdf.decrypt(password)
	    text=[]
	    for i in range(0,read_pdf.getNumPages()):
	    	text.append(read_pdf.getPage(i).extractText())
	    return ('\n'.join (text).replace("\n",''))
   
getTextPDF('sample-one-line.pdf')
