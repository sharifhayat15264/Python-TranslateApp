from docx import Document
from googletrans import Translator, LANGUAGES

langcodes = dict(map(reversed, LANGUAGES.items()))





driver("temp.docx", "French", "English")
