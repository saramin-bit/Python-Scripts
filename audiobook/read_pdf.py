from pyttsx3 import init
from PyPDF2 import PdfFileReader
from sys import argv, exit
from time import sleep


def read_pdf(pdf, reader):
    """
    Simple function for extract the text from a pdf file and read the text using text to speech engine
    :param pdf: path of the pdf file
    :param reader: text to speech engine object
    """
    with open(pdf, "rb") as doc:
        pdf_file_reader = PdfFileReader(doc)
        pages = pdf_file_reader.numPages
        print("Total page number in pdf: ", pages)
        try:
            start_from = int(input("Enter start page number [default: 0] : "))
        except ValueError:
            start_from = 0
        try:
            end = int(input(f"Enter end page number [default: End of the pdf page({pages})] : "))
        except ValueError:
            end = pages
        try:
            rate = int(input(f"If you assistant read the text faster than decrease the rate."
                             f"\nEnter the speed of voice. [default {reader.getProperty('rate')}] : "))
        except ValueError:
            rate = reader.getProperty("rate")
        finally:
            reader.setProperty("rate", rate)

        for page in range(start_from, end):
            pdf_page = pdf_file_reader.getPage(page)
            pdf_text = pdf_page.extractText()
            for line in pdf_text.splitlines():
                reader.say(line)
                reader.runAndWait()
                sleep(0.2)


if __name__ == '__main__':
    if not len(argv) == 2:
        exit("PDF path must be pass as argument")
    try:
        engine = init()
        read_pdf(argv[1], engine)
    except IOError:
        exit("Pdf file not found!")
    except KeyboardInterrupt:
        engine.stop()
        exit("\nStop Reading!\n")