from googletrans import Translator, LANGUAGES

langcodes = dict(map(reversed, LANGUAGES.items()))

def translate_text(text, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    for k, v in langcodes.items():
        if dest_lang == k:
            dest_code = v

    for k, v in langcodes.items():
        if src_lang == k:
            src_code = v

    translator = Translator()
    translated = translator.translate(str(text), dest_code, src_code)
    translation = translated.text
    print(translation)




