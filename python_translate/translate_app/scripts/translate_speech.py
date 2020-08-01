from django.conf import settings
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
import pyttsx3

path = settings.MEDIA_URL
langcodes = dict(map(reversed, LANGUAGES.items()))

language_code_dict = {"Afrikaans (South Africa)": "af-ZA", "Albanian (Albania)": "sq-AL",
                      "Amharic (Ethiopia)": "am-ET", "Arabic (Algeria)": "ar-DZ",
                      "Arabic (Bahrain)": "ar-BH", "Arabic (Egypt)": "ar-EG", "Arabic (Iraq)": "ar-IQ",
                      "Arabic (Israel)": "ar-IL", "Arabic (Jordan)": "ar-JO", "Arabic (Kuwait)": "ar-KW",
                      "Arabic (Lebanon)": "ar-LB", "Arabic (Morocco)": "ar-MA", "Arabic (Oman)": "ar-OM",
                      "Arabic (Qatar)": "ar-QA", "Arabic (Saudi Arabia)": "ar-SA",
                      "Arabic (State of Palestine)": "ar-PS", "Arabic (Tunisia)": "ar-TN",
                      "Arabic (United Arab Emirates)": "ar-AE", "Arabic (Yemen)": "ar-YE",
                      "Armenian (Armenia)": "hy-AM", "Azerbaijani (Azerbaijan)": "az-AZ",
                      "Basque (Spain)": "eu-ES", "Bengali (Bangladesh)": "bn-BD",
                      "Bengali (India)": "bn-IN", "Bosnian (Bosnia and Herzegovina)": "bs-BA",
                      "Bulgarian (Bulgaria)": "bg-BG", "Burmese (Myanmar)": "my-MM",
                      "Catalan (Spain)": "ca-ES", "Chinese, Cantonese (Traditional Hong Kong)": "yue-Hant-HK",
                      "Chinese, Mandarin (Simplified, China)": "zh (cmn-Hans-CN)",
                      "Chinese, Mandarin (Traditional, Taiwan)": "zh-TW (cmn-Hant-TW)",
                      "Croatian (Croatia)": "hr-HR", "Czech (Czech Republic)": "cs-CZ",
                      "Danish (Denmark)": "da-DK", "Dutch (Belgium)": "nl-BE",
                      "Dutch (Netherlands)": "nl-NL", "English (Australia)": "en-AU",
                      "English (Canada)": "en-CA", "English (Ghana)": "en-GH",
                      "English (Hong Kong)": "en-HK", "English (India)": "en-IN",
                      "English (Ireland)": "en-IE", "English (Kenya)": "en-KE",
                      "English (New Zealand)": "en-NZ", "English (Nigeria)": "en-NG",
                      "English (Pakistan)": "en-PK", "English (Philippines)": "en-PH",
                      "English (Singapore)": "en-SG", "English (South Africa)": "en-ZA",
                      "English (Tanzania)": "en-TZ", "English (United Kingdom)": "en-GB",
                      "English (United States)": "en-US", "Estonian (Estonia)": "et-EE",
                      "Filipino (Philippines)": "fil-PH", "Finnish (Finland)": "fi-FI",
                      "French (Belgium)": "fr-BE", "French (Canada)": "fr-CA", "French (France)": "fr-FR",
                      "French (Switzerland)": "fr-CH", "Galician (Spain)": "gl-ES",
                      "Georgian (Georgia)": "ka-GE", "German (Austria)": "de-AT",
                      "German (Germany)": "de-DE", "German (Switzerland)": "de-CH",
                      "Greek (Greece)": "el-GR", "Gujarati (India)": "gu-IN", "Hebrew (Israel)": "iw-IL",
                      "Hindi (India)": "hi-IN", "Hungarian (Hungary)": "hu-HU",
                      "Icelandic (Iceland)": "is-IS", "Indonesian (Indonesia)": "id-ID",
                      "Italian (Italy)": "it-IT", "Italian (Switzerland)": "it-CH",
                      "Japanese (Japan)": "ja-JP", "Javanese (Indonesia)": "jv-ID",
                      "Kannada (India)": "kn-IN", "Khmer (Cambodia)": "km-KH",
                      "Korean (South Korea)": "ko-KR", "Lao (Laos)": "lo-LA", "Latvian (Latvia)": "lv-LV",
                      "Lithuanian (Lithuania)": "lt-LT", "Macedonian (North Macedonia)": "mk-MK",
                      "Malay (Malaysia)": "ms-MY", "Malayalam (India)": "ml-IN", "Marathi (India)": "mr-IN",
                      "Mongolian (Mongolia)": "mn-MN", "Nepali (Nepal)": "ne-NP",
                      "Norwegian Bokmål (Norway)": "no-NO", "Persian (Iran)": "fa-IR",
                      "Polish (Poland)": "pl-PL", "Portuguese (Brazil)": "pt-BR",
                      "Portuguese (Portugal)": "pt-PT", "Punjabi (Gurmukhi India)": "pa-Guru-IN",
                      "Romanian (Romania)": "ro-RO", "Russian (Russia)": "ru-RU",
                      "Serbian (Serbia)": "sr-RS", "Sinhala (Sri Lanka)": "si-LK",
                      "Slovak (Slovakia)": "sk-SK", "Slovenian (Slovenia)": "sl-SI",
                      "Spanish (Argentina)": "es-AR", "Spanish (Bolivia)": "es-BO",
                      "Spanish (Chile)": "es-CL", "Spanish (Colombia)": "es-CO",
                      "Spanish (Costa Rica)": "es-CR", "Spanish (Dominican Republic)": "es-DO",
                      "Spanish (Ecuador)": "es-EC", "Spanish (El Salvador)": "es-SV",
                      "Spanish (Guatemala)": "es-GT", "Spanish (Honduras)": "es-HN",
                      "Spanish (Mexico)": "es-MX", "Spanish (Nicaragua)": "es-NI",
                      "Spanish (Panama)": "es-PA", "Spanish (Paraguay)": "es-PY", "Spanish (Peru)": "es-PE",
                      "Spanish (Puerto Rico)": "es-PR", "Spanish (Spain)": "es-ES",
                      "Spanish (United States)": "es-US", "Spanish (Uruguay)": "es-UY",
                      "Spanish (Venezuela)": "es-VE", "Sundanese (Indonesia)": "su-ID",
                      "Swahili (Kenya)": "sw-KE", "Swahili (Tanzania)": "sw-TZ",
                      "Swedish (Sweden)": "sv-SE", "Tamil (India)": "ta-IN", "Tamil (Malaysia)": "ta-MY",
                      "Tamil (Singapore)": "ta-SG", "Tamil (Sri Lanka)": "ta-LK", "Telugu (India)": "te-IN",
                      "Thai (Thailand)": "th-TH", "Turkish (Turkey)": "tr-TR",
                      "Ukrainian (Ukraine)": "uk-UA", "Urdu (India)": "ur-IN", "Urdu (Pakistan)": "ur-PK",
                      "Uzbek (Uzbekistan)": "uz-UZ", "Vietnamese (Vietnam)": "vi-VN",
                      "Zulu (South Africa)": "zu-ZA"}


def speech_to_text(audio_file, lang="en-US"):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        result = r.recognize_google(audio, language=lang)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        result = ''
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        result = ''

    return result


def translate_text(text, dest_code, src_code):
    translator = Translator()
    translated = translator.translate(str(text), dest_code, src_code)
    translation = translated.text
    return translation


def text_to_speech(translated_text, filename):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print("Voice: ")
    #     print(" - ID: %s" % voice.id)
    #     print(" - Name: %s" % voice.name)
    #     print(" - Languages: %s" % voice.languages)
    #     print(" - Gender: %s" % voice.gender)
    #     print(" - Age: %s" % voice.age)

    voice_id = voices[0].id
    engine.setProperty('voice', voice_id)

    engine.save_to_file(translated_text, filename)
    engine.say(translated_text)

    engine.runAndWait()
    return


def translate_speech(audio_file, dest_lang, src_lang):
    dest_code = language_code_dict[dest_lang]
    src_code = language_code_dict[src_lang]

    result = speech_to_text(audio_file, src_code)  # Specify language, record sound and generate text.
    print(result)

    if result:
        translation = translate_text(result, dest_code.split("-")[0], src_code.split("-")[0])  # Use the text to get translation
        print(translation)
    else:
        translation = ''

    text_to_speech(translation, audio_file)  # Output translation as audio
    return audio_file, translation
