import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
book = open('bose.pdf','rb')              # name of the file you want to read out (with path)
pdfreader = PyPDF2.PdfFileReader(book)    # create a file object
pages = pdfreader.numPages                # get num of pages in our file
print(pages)

page = pdfreader.getPage(17)              # select a page by number
text = page.extractText()                 # get the text from our file
speaker.say(text)                         # convert the text into speech
speaker.runAndWait()                      # run untill finish