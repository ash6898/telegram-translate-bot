from googletrans import Translator
def translate(to_translate):
    translator = Translator()
    try:
        translated = translator.translate(to_translate,dest='ta')
        return translated.text
    except:
        return to_translate
