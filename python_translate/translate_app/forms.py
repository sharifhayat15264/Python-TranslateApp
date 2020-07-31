from django import forms

languages = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali',
             'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)',
             'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino',
             'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole',
             'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish',
             'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz',
             'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam',
             'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto',
             'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian',
             'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese',
             'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur',
             'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']

speech_languages = ['Afrikaans (South Africa)', 'Albanian (Albania)', 'Amharic (Ethiopia)', 'Arabic (Algeria)',
                    'Arabic (Bahrain)', 'Arabic (Egypt)', 'Arabic (Iraq)', 'Arabic (Israel)', 'Arabic (Jordan)',
                    'Arabic (Kuwait)', 'Arabic (Lebanon)', 'Arabic (Morocco)', 'Arabic (Oman)', 'Arabic (Qatar)',
                    'Arabic (Saudi Arabia)', 'Arabic (State of Palestine)', 'Arabic (Tunisia)',
                    'Arabic (United Arab Emirates)', 'Arabic (Yemen)', 'Armenian (Armenia)', 'Azerbaijani (Azerbaijan)',
                    'Basque (Spain)', 'Bengali (Bangladesh)', 'Bengali (India)', 'Bosnian (Bosnia and Herzegovina)',
                    'Bulgarian (Bulgaria)', 'Burmese (Myanmar)', 'Catalan (Spain)',
                    'Chinese, Cantonese (Traditional Hong Kong)', 'Chinese, Mandarin (Simplified, China)',
                    'Chinese, Mandarin (Traditional, Taiwan)', 'Croatian (Croatia)', 'Czech (Czech Republic)',
                    'Danish (Denmark)', 'Dutch (Belgium)', 'Dutch (Netherlands)', 'English (Australia)',
                    'English (Canada)', 'English (Ghana)', 'English (Hong Kong)', 'English (India)',
                    'English (Ireland)', 'English (Kenya)', 'English (New Zealand)', 'English (Nigeria)',
                    'English (Pakistan)', 'English (Philippines)', 'English (Singapore)', 'English (South Africa)',
                    'English (Tanzania)', 'English (United Kingdom)', 'English (United States)', 'Estonian (Estonia)',
                    'Filipino (Philippines)', 'Finnish (Finland)', 'French (Belgium)', 'French (Canada)',
                    'French (France)', 'French (Switzerland)', 'Galician (Spain)', 'Georgian (Georgia)',
                    'German (Austria)', 'German (Germany)', 'German (Switzerland)', 'Greek (Greece)',
                    'Gujarati (India)','Hebrew (Israel)', 'Hindi (India)', 'Hungarian (Hungary)', 'Icelandic (Iceland)',
                    'Indonesian (Indonesia)', 'Italian (Italy)', 'Italian (Switzerland)', 'Japanese (Japan)',
                    'Javanese (Indonesia)', 'Kannada (India)', 'Khmer (Cambodia)', 'Korean (South Korea)', 'Lao (Laos)',
                    'Latvian (Latvia)', 'Lithuanian (Lithuania)', 'Macedonian (North Macedonia)', 'Malay (Malaysia)',
                    'Malayalam (India)', 'Marathi (India)', 'Mongolian (Mongolia)', 'Nepali (Nepal)',
                    'Norwegian Bokmål (Norway)', 'Persian (Iran)', 'Polish (Poland)', 'Portuguese (Brazil)',
                    'Portuguese (Portugal)', 'Punjabi (Gurmukhi India)', 'Romanian (Romania)', 'Russian (Russia)',
                    'Serbian (Serbia)', 'Sinhala (Sri Lanka)', 'Slovak (Slovakia)', 'Slovenian (Slovenia)',
                    'Spanish (Argentina)', 'Spanish (Bolivia)', 'Spanish (Chile)', 'Spanish (Colombia)',
                    'Spanish (Costa Rica)', 'Spanish (Dominican Republic)', 'Spanish (Ecuador)',
                    'Spanish (El Salvador)', 'Spanish (Guatemala)', 'Spanish (Honduras)', 'Spanish (Mexico)',
                    'Spanish (Nicaragua)', 'Spanish (Panama)', 'Spanish (Paraguay)', 'Spanish (Peru)',
                    'Spanish (Puerto Rico)', 'Spanish (Spain)', 'Spanish (United States)', 'Spanish (Uruguay)',
                    'Spanish (Venezuela)', 'Sundanese (Indonesia)', 'Swahili (Kenya)', 'Swahili (Tanzania)',
                    'Swedish (Sweden)', 'Tamil (India)', 'Tamil (Malaysia)', 'Tamil (Singapore)', 'Tamil (Sri Lanka)',
                    'Telugu (India)', 'Thai (Thailand)', 'Turkish (Turkey)', 'Ukrainian (Ukraine)', 'Urdu (India)',
                    'Urdu (Pakistan)', 'Uzbek (Uzbekistan)', 'Vietnamese (Vietnam)', 'Zulu (South Africa)']

CHOICES = [(x, x.capitalize()) for x in languages]
SPEECH_CHOICES = [(x, x) for x in speech_languages]


# creating a text translation form
class TextForm(forms.Form):
    source = forms.Select(choices=CHOICES)
    destination = forms.Select(choices=CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)


class FileForm(forms.Form):
    source = forms.Select(choices=CHOICES)
    destination = forms.Select(choices=CHOICES)
    upload_file = forms.FileField()


class SpeechForm(forms.Form):
    source = forms.Select(choices=SPEECH_CHOICES)
    destination = forms.Select(choices=SPEECH_CHOICES)
    audio_file = forms.FileField()
