
from helpers import PronounRemover
from helpers import ParsedTextToDataTable
from helpers import TextParser
import Tkinter

print("Welcolme to This Version of Text_Analysis...\n")
print("Please Input the Text You Would Like To Analyse\n")
text = raw_input("")

#text = PronounRemover.Process(text)

print("Here's what we got\n")

structured_sentences = TextParser.Process(text)
#print structured_sentences
#for structured_sentence in structured_sentences:
#    structured_sentence.draw()

print("Generating Data Tree!")
ParsedTextToDataTable.Process(structured_sentences,text)

