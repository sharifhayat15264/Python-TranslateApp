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

def translate_long_text(text, dest_lang, src_lang):
    n = 14900
    text_list = [(text[i:i + n]) for i in range(0, len(text), n)]
    translation_list = list()
    translator = Translator()
    for t in text_list:
        translated = translator.translate(str(t), dest_code, src_code)
        translation = translated.text
        translation_list.append(translation)

    complete_translation = "".join(translation_list)
    return complete_translation



sample = "These excellant intentions were strengthed when he enterd the Father Superior's diniing-room, though, stricttly speakin, it was not a dining-room, for the Father Superior had only two rooms alltogether; they were, however, much larger and more comfortable than Father Zossima's. But tehre was was no great luxury about the furnishng of these rooms eithar. The furniture was of mohogany, covered with leather, in the old-fashionned style of 1820 the floor was not even stained, but evreything was shining with cleanlyness, and there were many chioce flowers in the windows; the most sumptuous thing in the room at the moment was, of course, the beatifuly decorated table. The cloth was clean, the service shone; there were three kinds of well-baked bread, two bottles of wine, two of excellent mead, and a large glass jug of kvas -- both the latter made in the monastery, and famous in the neigborhood. There was no vodka. Rakitin related afterwards that there were five dishes: fish-suop made of sterlets, served with little fish paties; then boiled fish served in a spesial way; then salmon cutlets, ice pudding and compote, and finally, blanc-mange. Rakitin found out about all these good things, for he could not resist peeping into the kitchen, where he already had a footing. He had a footting everywhere, and got informaiton about everything. He was of an uneasy and envious temper. He was well aware of his own considerable abilities, and nervously exaggerated them in his self-conceit. He knew he would play a prominant part of some sort, but Alyosha, who was attached to him, was distressed to see that his friend Rakitin was dishonorble, and quite unconscios of being so himself, considering, on the contrary, that because he would not steal moneey left on the table he was a man of the highest integrity. Neither Alyosha nor anyone else could have infleunced him in that."
# a = translate_text(sample, "French", "English")
print(len(sample))