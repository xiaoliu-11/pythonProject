import PyPDF2
import sys
#filepath = "C:\\Users\\Administrator\\Desktop\\est.pdf"
filepath = "ss.pdf"
pdffile = PyPDF2.PdfFileReader(open(filepath,'rb'))
metadata = pdffile.getDocumentInfo()
for key in metadata:
    print(key,":",metadata[key])