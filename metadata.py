#!/usr/bin/env python3

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

fin = None
reader = None
writer = None
pdfPath = None

def load_pdf(f):
    global fin, reader
    fin = open(f, 'rb')
    reader = PdfFileReader(fin)

def get_metadata():
    global reader
    return reader.getDocumentInfo()

def editTitle(text):
    global writer, reader, pdfPath, fin

    try:
        oldmetadata = get_metadata()

        writer = PdfFileWriter()
        writer.appendPagesFromReader(reader)
        writer.addMetadata(oldmetadata)
        writer.addMetadata({
            '/Title': text
        })

        fout = open(pdfPath, 'ab')
        writer.write(fout)

        fin.close()
        fout.close()
    except Exception as e:
        print(e)
    finally:
        load_pdf(pdfPath)
        print("OK!\nChanged: {} \n\n TO: {}".format(oldmetadata, get_metadata()))

def main():
    if len(sys.argv) > 2:
        global pdfPath
        pdfPath = sys.argv[1]
        newTitle = sys.argv[2]

        load_pdf(pdfPath)
        editTitle(newTitle) 

main()