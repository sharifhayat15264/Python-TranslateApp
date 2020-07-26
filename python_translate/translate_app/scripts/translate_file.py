import PyPDF2
import nltk.data
from docx import Document
from googletrans import Translator, LANGUAGES

langcodes = dict(map(reversed, LANGUAGES.items()))


def translate_file(filename, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    dest_code = langcodes[dest_lang]
    src_code = langcodes[src_lang]

    try:
        with open(filename, "r", encoding="utf8") as txt_file:
            text = txt_file.read()

            # if text has 15K or more characters:
            if len(text) >= 15000:
                complete_translation = translate_long_text(text, dest_code, src_code)
                with open("result.txt", "w") as result:
                    result.write(complete_translation)
                    print("File Created!")
                    return
            else:
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


# PDF #
def translate_pdf(filename, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    dest_code = langcodes[dest_lang]
    src_code = langcodes[src_lang]

    try:
        with open(filename, "rb") as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            pages = reader.numPages
            text = ""
            for i in range(pages):
                page = reader.getPage(i)
                text += page.extractText()
            full_text = text.replace("\n", "")

            if len(full_text) >= 15000:
                complete_translation = translate_long_text(full_text, dest_code, src_code)
                with open("result_pdf.txt", "w") as result:
                    result.write(complete_translation)
                    print("File Created!")
                    return
            else:
                translator = Translator()
                translated = translator.translate(full_text, dest_code, src_code)
                translation = translated.text
                print(translation)
                with open("result_pdf.txt", "w") as result:
                    result.write(translation)
                    print("File Created!")
                    return

    except FileNotFoundError:
        print("File not found.")
        return

# translate_pdf("test.pdf", "German", "English")


# DOCS #
def get_text_docs(filename, dest_lang, src_lang):
    doc = Document(filename)
    full_text = list()
    for para in doc.paragraphs:
        full_text.append(para.text)

    text = '\n'.join(full_text)
    return text


def translate_docs(filename, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    dest_code = langcodes[dest_lang]
    src_code = langcodes[src_lang]

    text = get_text_docs(filename)

    if len(text) >= 15000:
        complete_translation = translate_long_text(text, dest_code, src_code)
        return complete_translation
    else:
        translator = Translator()
        translated = translator.translate(text, dest_code, src_code)
        translation = translated.text
        return translation


# call if text is very long
def translate_long_text(text, dest_code, src_code):
    # nltk code goes here bro
    valid_lang = {"cs" : "czech", "da" : "danish", "nl" : "dutch", "en" : "english", "et" : "estonian",
                         "fi" : "finnish", "fr" : "french", "de" : "german", "el" : "greek", "it" : "italian",
                         "no" : "norwegian", "pl" : "polish", "pt" : "portuguese", "ru" : "russian", "sl" : "slovene",
                         "es" : "spanish", "sv" : "swedish", "tr" : "turkish"}

    if src_code in valid_lang:
        src_language = valid_lang[src_code]
        src_tokenizer = nltk.data.load(f"tokenizers\punkt\{src_language}.pickle")
        text_list = src_tokenizer.tokenize(text)
        with open("tokens.txt", "w") as token:
            token.write(str(text_list))
    else:
        print("Not a recognized source language for long translation")
        return 1

    translator = Translator()
    translation_list = []

    temp_str = ""
    total_len = 0
    for t in text_list:
        current_len = len(temp_str)
        total_len += len(t)
        print(current_len)
        if (current_len + len(t)) > 10000:
            print("translating...")
            translated = translator.translate(temp_str, dest_code, src_code)
            translation = translated.text
            translation_list.append(translation)
            temp_str = ""
        else:
            temp_str += " " + t

    translated = translator.translate(temp_str, dest_code, src_code)
    translation = translated.text
    translation_list.append(translation)

    print(len(translation_list))

    complete_translation = "".join(translation_list)
    return complete_translation


def generate_file(translation):
    with open("result.txt", "w") as f:
        f.write(translation)


def driver(filename, dest_lang, src_lang):
    translation = translate_docs(filename, dest_lang, src_lang)
    generate_file(translation)














# print(langcodes)
# with open("sample.txt", "r", encoding="utf8") as file:
#     text = file.read()
#     len_original = len(text)
#     result = translate_long_text(text, "fr", "en")
#     with open("result.txt", "w") as nigger:
#         nigger.write(result)

# with open("str_t.txt", "r") as file:
#     text = file.read()
#     translate_long_text(text, "fr", "en")