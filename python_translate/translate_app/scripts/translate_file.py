import PyPDF2

from googletrans import Translator, LANGUAGES

langcodes = dict(map(reversed, LANGUAGES.items()))

def translate_file(filename, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    dest_code = langcodes[dest_lang]

    src_code = langcodes[src_lang]

    try:
        with open(filename, "r") as txt_file:
            text = txt_file.read()
            translator = Translator()
            translated = translator.translate(text, dest_code, src_code)
            translation = translated.text
            print(translation)
            with open("result.txt", "w") as result:
                result.write(translation)
                print("File Created!")

    except FileNotFoundError:
        print("File not found")
        return

def translate_pdf(filename, dest_lang, src_lang):
    with open(filename, "rb") as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        print(reader.numPages)
        page = reader.getPage(0)
        text = page.extractText()
        #fulltext = '\n'.join(text)
        print(text)





# translate_pdf("test.pdf", "German", "English")
translate_file("try.txt", "German", "English")

# def getText(filename):
#     doc = docx.Document(filename)
#     full_text = list()
#     for para in doc.paragraphs:
#         full_text.append(para.text)
#     text = '\n'.join(full_text)
#     return text
#
#
# def translate_docs(filename, dest_lang, src_lang):
#     text = getText(filename)
#     translator = Translator()
#     translated = translator.translate(text, "fr", "en")
#     translation = translated.text
#     print(translation)






