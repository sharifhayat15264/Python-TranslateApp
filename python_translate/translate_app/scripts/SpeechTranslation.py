import speech_recognition as sr
from googletrans import Translator, LANGUAGES
import pyttsx3


langcodes = dict(map(reversed, LANGUAGES.items()))

def speech_to_text(lang="en-US"):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("speak now")
        audio = r.listen(source)
    result = r.recognize_google(audio, language=lang)
    print(result)
    return result



def translate_text(text, dest_lang, src_lang):
    dest_lang = dest_lang.lower()
    src_lang = src_lang.lower()

    dest_code = langcodes[dest_lang]
    src_code = langcodes[src_lang]

    translator = Translator()
    translated = translator.translate(str(text), dest_code, src_code)
    translation = translated.text
    return translation


def text_to_speech(translated_text):
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print("Voice: ")
    #     print(" - ID: %s" % voice.id)
    #     print(" - Name: %s" % voice.name)
    #     print(" - Languages: %s" % voice.languages)
    #     print(" - Gender: %s" % voice.gender)
    #     print(" - Age: %s" % voice.age)
    voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', voice_id)
    engine.say(translated_text)
    engine.runAndWait()
    return






result = speech_to_text() # Specify language, record sound and generate text.
translation = translate_text(result, "English", "French") # Use the text to get translation
print(translation)
text_to_speech(translation) # Output translation as audio

