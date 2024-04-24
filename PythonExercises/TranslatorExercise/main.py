from translate import Translator

translator= Translator(to_lang="ja")
translation = translator.translate("This is a pen.")
print(translation)