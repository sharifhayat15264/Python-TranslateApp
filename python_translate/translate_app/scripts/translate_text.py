from googletrans import Translator, LANGUAGES

langcodes = dict(map(reversed, LANGUAGES.items()))


def translate_text(text, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    dest_code = langcodes[dest_lang]
    src_code = langcodes[src_lang]

    translator = Translator()
    translated = translator.translate(str(text), dest_code, src_code)
    translation = translated.text
    return translation
